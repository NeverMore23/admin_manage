from django.db import models


# Create your models here.
class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    roles = models.ManyToManyField('Role', verbose_name='与角色多对多绑定')


class Role(models.Model):
    """
    角色表，多对多绑定权限
    """
    name = models.CharField(max_length=32, verbose_name='角色名称')
    Permissions = models.ManyToManyField('Permission', verbose_name='与权限多对多绑定')


class Permission(models.Model):
    """
    权限表
    """
    name = models.CharField(max_length=32, verbose_name='权限名称')
    url = models.CharField(max_length=32, verbose_name='对应路径')
    code = models.CharField(max_length=32, verbose_name='别名')
    menu_group = models.ForeignKey(to='Permission', related_name='xxx', null=True, blank=True, default=None,
                                   verbose_name='所属菜单组')
    PermissionGroup = models.ForeignKey('PermissionGroup', null=True, verbose_name='所属权限组')


class PermissionGroup(models.Model):
    """
    权限分组
    """
    name = models.CharField(max_length=32, verbose_name='权限组名称')
    Menu = models.ForeignKey('Menu', null=True, verbose_name='所属菜单')


class Menu(models.Model):
    """
    菜单
    """
    name = models.CharField(max_length=32, verbose_name='菜单名称')

'''
Role.objects.create(name='CEO')
Role.objects.create(name='总监')
Role.objects.create(name='经理')
Role.objects.create(name='业务员')

User.objects.create(username='番禺', password=123)
User.objects.create(username='鲁宁', password=123)
User.objects.create(username='肾松', password=123)
User.objects.create(username='文飞', password=123)
User.objects.create(username='成栋', password=123)

Menu.objects.create(name='菜单一')
Menu.objects.create(name='菜单二')

PermissionGroup.objects.create(name='用户组', menu_id=1)
PermissionGroup.objects.create(name='订单组', menu_id=2)

Permission.objects.create(url='/userinfo/', name='用户列表', permissionGroup_id=1, code='list')
Permission.objects.create(url='/userinfo/add/', name='添加用户', permissionGroup_id=1, code='add')
Permission.objects.create(url='/userinfo/edit/(\d+)/', name='编辑用户', permissionGroup_id=1, code='edit')
Permission.objects.create(url='/userinfo/del/(\d+)/', name='删除用户', permissionGroup_id=1, code='del')
Permission.objects.create(url='/order/', name='订单列表', permissionGroup_id=2, code='list')
Permission.objects.create(url='/order/add/', name='添加订单', permissionGroup_id=2, code='add')
Permission.objects.create(url='/order/edit/(\d+)/', name='编辑订单', permissionGroup_id=2, code='edit')
Permission.objects.create(url='/order/del/(\d+)/', name='删除订单', permissionGroup_id=2, code='del')

Role.objects.get(name='CEO').permissions.add(1, 2, 3, 4, 5, 6, 7, 8)
Role.objects.get(name='总监').permissions.add(1, 2, 5, 6)
Role.objects.get(name='经理').permissions.add(1, 5)
Role.objects.get(name='业务员').permissions.add(5)

User.objects.get(username='番禺').roles.add(1)
User.objects.get(username='鲁宁').roles.add(2)
User.objects.get(username='肾松').roles.add(3, 4)
User.objects.get(username='文飞').roles.add(4)
User.objects.get(username='成栋').roles.add(4)
'''


