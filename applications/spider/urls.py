from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/spider/running/spider$', views.running_spider, name=u'天天快听|动作事件'),
    url(r'^api/spider/get/img', views.get_img, name=u'天天快听|获取图片列表'),
    url(r'^spider/config', views.spider_config, name=u'天天快听|获取图片列表'),
]
