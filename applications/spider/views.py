from django.http import JsonResponse
from django.shortcuts import render

from utils.argument import get_parameter, catch_exception
from scripts import pic_spi


# Create your views here.


def running_spider(request):
    start_page = get_parameter('start_pate', required=True, formatter=int)
    page_numbers = get_parameter('page_numbers', required=True, formatter=int)

    settings = {
        "start_page": start_page,
        "page_num": page_numbers,
        "dir_name": "img",
        "url": 'https://601rr.com/tupian/{}.html',
        "path": "D:\\",
        "re": r'data-original_break="(.+?\.jpg)"'
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
