# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_rename_comment_to_pagecomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FrontLink',
            new_name='PageLink',
        ),
    ]
