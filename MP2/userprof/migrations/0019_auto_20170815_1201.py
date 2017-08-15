# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 04:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0018_auto_20170815_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprof.Post'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]