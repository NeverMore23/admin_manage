import re
from django.conf import settings
from django.shortcuts import HttpResponse, render, redirect


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_url = request.path_info
        # 白名单处理
        for url in settings.VALID_URLS:
            if re.match(url, current_url):
                return None

        # 当前用户的权限列表
        permission_dict = request.session.get(settings.PERMISSION_URL_KEY)
        if not permission_dict:
            return redirect('/login/')

        flag = False
        for group_id, codes_urls in permission_dict.items():
            for permission_url in codes_urls['urls']:
                regex = "^{0}$".format(permission_url)
                if re.match(regex, current_url):
                    request.permission_code_list = codes_urls['codes']
                    flag = True
                    break
            if flag:
                break

        if not flag:
            return HttpResponse('无权访问')
