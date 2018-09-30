# encoding:utf8
from django.contrib import admin
from advertising.models import Advertising
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['start_time']  # 按添加日期过滤
    search_fields = ['id']  # 按广告ID搜索
    list_per_page = 10  # 默认为10条
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    # actions_on_bottom = True
    # 定义列表中要显示哪些字段
    list_display = ('id', 'start_time', 'end_time')
    # 详细时间分层筛选　
    date_hierarchy = 'start_time'

VERBOSE_APP_NAME = u"广告图片"
admin.site.site_header = '北京源石智影--新闻广告资源管理系统'
admin.site.site_title = '北京源石智影有限公司'

# 注册模型类
admin.site.register(Advertising, ArticleAdmin)