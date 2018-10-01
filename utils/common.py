from django.db import models


class BaseModel(models.Model):
    STATUS_ENABLE = 1
    STATUS_DISABLE = -1

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        abstract = True
