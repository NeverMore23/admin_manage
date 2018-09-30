from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    """
    文章类别
    """
    name = models.CharField(max_length=10, verbose_name='名称')

    class Meta:
        db_table = 'tb_news_category'
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class NewsChannel(models.Model):
    """
    文章频道
    """
    group_id = models.IntegerField(verbose_name='组号')
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, verbose_name='顶级文章类别')
    url = models.CharField(max_length=50, verbose_name='频道页面链接')
    sequence = models.IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'tb_goods_channel'
        verbose_name = '文章频道'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name