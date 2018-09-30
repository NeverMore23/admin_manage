from django.contrib import admin
from . import models


# Register your models here.
class NewsCategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()

    def delete_model(self, request, obj):
        obj.delete()


# 注册model类
admin.site.register(models.NewsCategory, NewsCategoryAdmin)