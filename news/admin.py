# encoding:utf-8
from django.contrib import admin
from news.models import News


# actions添加模型动作
def disable_status(modeladmin, request, queryset):
    queryset.update(is_enable=False)


def enable_status(modeladmin, request, queryset):
    queryset.update(is_enable=True)

disable_status.short_description = '隐藏文章'
enable_status.short_description = '显示文章'


class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['timestamp']  # 按添加日期过滤
    search_fields = ['title']  # 按文章题目搜索
    list_per_page = 100  # 默认为10条
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    # actions_on_bottom = True
    # 定义列表中要显示哪些字段
    list_display = ('title', 'publisher', 'timestamp', 'tag', 'parent')
    # 详细时间分层筛选　
    date_hierarchy = 'timestamp'
    # list_editable 设置默认可编辑字段
    list_editable = ['tag', 'parent']
    # 显示，隐藏的动作
    actions = [disable_status, enable_status]

VERBOSE_APP_NAME = u"新闻文章"
admin.site.site_header = '北京源石智影--新闻广告资源管理系统'
admin.site.site_title = '北京源石智影有限公司'


# 注册Model类
admin.site.register(News, ArticleAdmin)


# class TagGroupAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     fieldsets = (
#         (None, {'fields': ('name', 'tags')}),
#     )
#     filter_horizontal = ('tags',)
#
#
# # 注册model 类
# admin.site.register(TagGroup, TagGroupAdmin)