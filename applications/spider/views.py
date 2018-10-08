<<<<<<< HEAD
=======
# coding:utf-8
>>>>>>> 0c80e8dc36abf3cc7feae9621664145a3496a82b
from django.http import JsonResponse
from django.shortcuts import render

from utils.argument import get_parameter, catch_exception
from scripts import pic_spi


# Create your views here.
<<<<<<< HEAD


def running_spider(request):
    start_page = get_parameter('start_pate', required=True, formatter=int)
    page_numbers = get_parameter('page_numbers', required=True, formatter=int)
=======
def spider_config(request):
    return render(request, 'spider/spider_config.html')


#   优化：使用异步
def running_spider(request):
    start_page = get_parameter(request, name='start_page', formatter=int)
    page_numbers = get_parameter(request, name='page_numbers', formatter=int)
    dir_name = get_parameter(request, name='dir_name')
    path = get_parameter(request, name='path')

    if not start_page:
        start_page = 14005
    if not page_numbers:
        page_numbers = 1
    if not dir_name:
        dir_name = "cmg",
    if not path:
        path = "D:\\",
>>>>>>> 0c80e8dc36abf3cc7feae9621664145a3496a82b

    settings = {
        "start_page": start_page,
        "page_num": page_numbers,
<<<<<<< HEAD
        "dir_name": "img",
        "url": 'https://601rr.com/tupian/{}.html',
        "path": "D:\\",
        "re": r'data-original_break="(.+?\.jpg)"'
=======
        "dir_name": dir_name,
        "url": 'https://www.902ff.com/tupian//{}.html',
        "path": path,
        "re": r'data-original="(.+?\.jpg)"',
        "running": False,
>>>>>>> 0c80e8dc36abf3cc7feae9621664145a3496a82b
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
