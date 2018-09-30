# encoding:utf-8
from django.db import models
from ckeditor.fields import RichTextField
from category.models import NewsCategory


class News(models.Model):
    """文章"""
    __tablename__ = "users_news"

    id = models.IntegerField(primary_key=True, verbose_name='文章编号')  # 新闻编号
    title = models.CharField(max_length=200, verbose_name='文章标题')  # 新闻标题
    content = RichTextField(null=False, verbose_name='文章内容')  # 新闻内容
    status = models.IntegerField(default=0, verbose_name='审核状态')  #当前新闻状态 如果为0代表审核通过，1代表审核中，-1代表审核不通过
    reason = models.CharField(max_length=200, verbose_name='未通过原因')  # 未通过原因，status = -1 的时候使用
    timestamp = models.DateTimeField(verbose_name='发布日期', default="") # 发布日期
    tag = models.CharField(max_length=200, verbose_name='标签', default='') # 关键字标签
    publisher = models.CharField(max_length=200, verbose_name='发布人', default='')  # 发布人
    parent = models.ForeignKey(NewsCategory, null=True, blank=True, on_delete=models.CASCADE, verbose_name='所属类别')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # 为我们创建的模型类和属性加上中文名称
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'  # 设置复数的显示，否则会出现“文章s”


# Create your models here.
# class Tag(models.Model):
#     """
#     一个关键字
#     """
#     id = models.IntegerField(primary_key=True, verbose_name='标签编号')  # 标签编号
#     name = models.CharField(max_length=200, verbose_name='标签内容', default='') # 标签内容
#
#
# class TagGroup(models.Model):
#     """多个关键字"""
#     name = models.CharField(max_length=64)
#     tags = models.ManyToManyField(Tag, max_length=200, verbose_name='标签', blank=True)  # 关键字标签
#
#     def __unicode__(self):
#         return self.name

