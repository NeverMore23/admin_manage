from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from utils.common import BaseModel


# Create your models here.


class Ads(BaseModel):
    """广告"""
    __tablename__ = "ads"

    id = models.IntegerField(primary_key=True, verbose_name='广告编号')
    content = RichTextUploadingField(null=False, verbose_name='广告内容')
    # image = models.ImageField(upload_to='Advertising', verbose_name='图片', null=True)
    hyperlinks = models.CharField(max_length=200, verbose_name='跳转页面url', default='')

    def __unicode__(self):
        return self.id

    def __int__(self):
        return self.id

    # 为我们创建的模型类和属性加上中文名称
    class Meta:
        db_table = 't_ads'
        verbose_name = '广告'
        verbose_name_plural = '广告'


class ArticlesCategory(BaseModel):
    """
    文章类别
    """
    name = models.CharField(max_length=10, verbose_name='名称')

    class Meta:
        db_table = 't_articles_category'
        verbose_name = '类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Articles(BaseModel):
    STATUS_PASS = 1
    STATUS_FAIL = -1
    STATUS_CHECKING = 2

    """文章"""
    __tablename__ = "articles"

    id = models.IntegerField(primary_key=True, verbose_name='文章编号')
    title = models.CharField(max_length=200, verbose_name='文章标题')
    content = RichTextField(null=False, verbose_name='文章内容')
    status = models.IntegerField(default=0, verbose_name='审核状态')
    reason = models.CharField(max_length=200, verbose_name='未通过原因')
    tag = models.CharField(max_length=200, verbose_name='标签', default='')
    publisher = models.CharField(max_length=200, verbose_name='发布人', default='')
    parent = models.ForeignKey(ArticlesCategory, null=True, blank=True, on_delete=models.CASCADE, verbose_name='所属类别')
    is_enable = models.BooleanField(verbose_name='状态', default=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        db_table = 't_articles'
        verbose_name = '文章'
        verbose_name_plural = '文章'


class ArticlesChannel(BaseModel):
    """
    文章频道
    """
    group_id = models.IntegerField(verbose_name='组号')
    category = models.ForeignKey(ArticlesCategory, on_delete=models.CASCADE, verbose_name='顶级文章类别')
    url = models.CharField(max_length=50, verbose_name='频道页面链接')
    sequence = models.IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'tb_articles_channel'
        verbose_name = '文章频道'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name