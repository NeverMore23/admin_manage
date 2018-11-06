from django.shortcuts import render, redirect, HttpResponse
from RBAC.models import UserInfo
from RBAC.service.init_permission import init_permission


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return render(request, "login.html", {'error': '用户名或密码错误！'})
        else:
            init_permission(request, user_obj) #调用init_permission，初始化权限
            return redirect('/index/')
