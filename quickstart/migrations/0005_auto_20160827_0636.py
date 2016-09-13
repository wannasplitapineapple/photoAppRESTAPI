# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-27 06:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0004_snippet_upvotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='downVotes',
            field=models.ManyToManyField(related_name='downVotedOn', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='upVotes',
            field=models.ManyToManyField(related_name='upVotedOn', to=settings.AUTH_USER_MODEL),
        ),
    ]
