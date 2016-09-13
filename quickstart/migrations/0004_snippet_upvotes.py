# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-26 10:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0003_auto_20160826_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='upVotes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
