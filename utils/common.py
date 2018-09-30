from django.db import models


class BaseModel(models.Model):
    STATUS_ENABLE = 1
    STATUS_DISABLE = -1

    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
