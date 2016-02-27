# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0003_rename_frontlink_to_pagelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelink',
            name='likes_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pagecomment',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pageComments', to='frontpage.PageLink'),
        ),
    ]
