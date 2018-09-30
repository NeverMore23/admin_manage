# encoding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from category.models import NewsCategory


class Advertising(models.Model):
    """图片广告"""
    __tablename__ = "advertising"

    id = models.IntegerField(primary_key=True, verbose_name='广告编号')  # 广告编号
    content = RichTextUploadingField(null=False, verbose_name='广告内容')  # 广告内容
    # image = models.ImageField(upload_to='Advertising', verbose_name='图片', null=True)
    start_time = models.DateTimeField(verbose_name='开始日期', default="") # 开始日期
    end_time = models.DateTimeField(verbose_name='结束日期',  default='') # 结束日期
    # 跳转链接
    hyperlinks = models.CharField(max_length=200, verbose_name='跳转页面url', default='')
    parent = models.ForeignKey(NewsCategory, null=True, blank=True, on_delete=models.CASCADE, verbose_name='所属类别')

    def __unicode__(self):
        return self.id

    def __int__(self):
        return self.id

    # 为我们创建的模型类和属性加上中文名称
    class Meta:
        verbose_name = '广告图片'
        verbose_name_plural = '广告'  # 设置复数的显示，否则会出现“广告s”
