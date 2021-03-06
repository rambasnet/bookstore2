# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(db_index=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterIndexTogether(
            name='author',
            index_together=set([('id', 'slug')]),
        ),
    ]
