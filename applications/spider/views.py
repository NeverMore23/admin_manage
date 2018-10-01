# coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render

from utils.argument import get_parameter, catch_exception
from scripts import pic_spi


# Create your views here.
def spider_config(request):
    return render(request, 'spider/spider_config.html')


#   优化：使用异步
def running_spider(request):
    start_page = get_parameter(request, name='start_pate', formatter=int)
    page_numbers = get_parameter(request, name='page_numbers', formatter=int)
    dir_name = get_parameter(request, name='dir_name')
    path = get_parameter(request, name='path')

    if not start_page:
        start_page = 14000
    if not page_numbers:
        page_numbers = 1
    if not dir_name:
        dir_name = "cmg",
    if not path:
        path = "D:\\",

    settings = {
        "start_page": start_page,
        "page_num": page_numbers,
        "dir_name": dir_name,
        "url": 'https://www.902ff.com/tupian//{}.html',
        "path": path,
        "re": r'data-original="(.+?\.jpg)"'
    }

    spider = pic_spi.Spider(settings)
    spider.run()

    result = {
        'code': 0,
        'msg': ''
    }
    return JsonResponse(result)


def get_img(request):
    pass
