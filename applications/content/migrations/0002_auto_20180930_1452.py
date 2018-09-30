# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-30 14:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='广告内容')),
            ],
            options={
                'verbose_name_plural': '广告',
                'db_table': 't_ads',
                'verbose_name': '广告',
            },
        ),
        migrations.DeleteModel(
            name='AAA',
        ),
    ]
