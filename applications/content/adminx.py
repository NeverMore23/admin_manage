import xadmin
from xadmin import views

from content.models import Ads, Articles, ArticlesCategory, ArticlesChannel


class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "媒体资源管理系统"  # 设置站点标题
    site_footer = "北京源石智影有限公司"  # 设置站点的页脚
    # menu_style = "accordion"  # 设置菜单折叠


# actions添加模型动作
def disable_status(modeladmin, request, queryset):
    queryset.update(is_enable=False)


def enable_status(modeladmin, request, queryset):
    queryset.update(is_enable=True)


disable_status.short_description = '隐藏文章'
enable_status.short_description = '显示文章'


class AdsAdmin(object):
    model_icon = 'fa fa-gift'
    list_filter = ['create_time']  # 按添加日期过滤
    search_fields = ['id']  # 按广告ID搜索
    list_per_page = 10  # 默认为10条
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    # actions_on_bottom = True
    # 定义列表中要显示哪些字段
    list_display = ('id', 'create_time', 'modify_time')
    # 详细时间分层筛选　
    date_hierarchy = 'create_time'


class ArticlesAdmin(object):
    model_icon = 'fa fa-gift'
    list_filter = ['create_time']  # 按添加日期过滤
    search_fields = ['title']  # 按文章题目搜索
    list_per_page = 100  # 默认为10条
    # 显示顶部的选项
    actions_on_top = True
    # 显示底部的选项
    # actions_on_bottom = True
    # 定义列表中要显示哪些字段
    list_display = ('title', 'publisher', 'create_time', 'tag', 'parent')
    # 详细时间分层筛选　
    date_hierarchy = 'create_time'
    # list_editable 设置默认可编辑字段
    list_editable = ['tag', 'parent']
    # 显示，隐藏的动作
    actions = [disable_status, enable_status]


class ArticlesCategoryAdmin(object):
    model_icon = 'fa fa-gift'

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()


class ArticlesChannelAdmin(object):
    model_icon = 'fa fa-gift'

    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()


xadmin.site.register(Ads, AdsAdmin)
xadmin.site.register(Articles, ArticlesAdmin)
xadmin.site.register(ArticlesCategory, ArticlesCategoryAdmin)
xadmin.site.register(ArticlesChannel, ArticlesChannelAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
