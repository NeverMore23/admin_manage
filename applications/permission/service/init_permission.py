from collections import defaultdict
from django.conf import settings


def init_permission(request, user):
    # 查询登录用户的权限等信息
    current_url = request.path_info
    userdata = user.roles.values('permissions__id'  # 权限ID
                                 , 'permissions__name'  # 权限名称
                                 , 'permissions__code'  # 别名
                                 , 'permissions__url'  # 权限路径
                                 , 'permissions__menu_group_id'  # 组内菜单ID，Null表示是菜单
                                 , 'permissions__permissionGroup_id'  # 权限所属组ID
                                 , 'permissions__permissionGroup__menu_id'  # 菜单ID
                                 , 'permissions__permissionGroup__menu__name'  # 菜单名称
                                 ).distinct()
    # 权限相关
    """
    permission_url_dict数据结构如下
    {
        1: {
            'codes': ['list', 'add', 'edit', 'del'], 
            'urls': ['/userinfo/', '/userinfo/add/', '/userinfo/edit/(\\d+)/', '/userinfo/del/(\\d+)/']
        },
        2: {
            'codes': ['list', 'add', 'edit', 'del'], 
            'urls': ['/order/', '/order/add/', '/order/edit/(\\d+)/', '/order/del/(\\d+)/']
        }
    }
    """
    permission_url_dict = defaultdict(lambda: {'codes': [], 'urls': []})
    for item in userdata:
        permission_url_dict[item['permissions__permissionGroup_id']]['codes'].append(item['permissions__code'])
        permission_url_dict[item['permissions__permissionGroup_id']]['urls'].append(item['permissions__url'])

    request.session[settings.PERMISSION_URL_KEY] = permission_url_dict  # 用户的权限信息保存到session中

    # 菜单相关
    """
    permission_menu_list 数据结构如下
    [
        {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单一'}, 
        {'id': 2, 'title': '添加用户', 'url': '/userinfo/add/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'}, 
        {'id': 3, 'title': '编辑用户', 'url': '/userinfo/edit/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'}, 
        {'id': 4, 'title': '删除用户', 'url': '/userinfo/del/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title':'菜单一'}, 
        {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单二'}, 
        {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'},
        {'id': 7, 'title': '编辑订单', 'url': '/order/edit/(\\d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}, 
        {'id': 8, 'title': '删除订单', 'url': '/order/del/(\\d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}
    ]
    """
    # 初步处理数据，在自定义标签中生成左侧菜单数据
    permission_menu_list = []
    for item in userdata:
        tpl = {
            'id': item['permissions__id'],
            'title': item['permissions__name'],
            'url': item['permissions__url'],
            'menu_gp_id': item['permissions__menu_group_id'],
            'menu_id': item['permissions__permissionGroup__menu_id'],
            'menu_title': item['permissions__permissionGroup__menu__name'],
        }
        permission_menu_list.append(tpl)
    request.session[settings.PERMISSION_MENU_KEY] = permission_menu_list  # 用户的菜单信息保存到session中
