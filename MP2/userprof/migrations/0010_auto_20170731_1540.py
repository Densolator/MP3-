# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0009_post_academic_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Academic', 'Academic'), ('Non-Academic', 'Non-Academic')], default='Academic', max_length=20),
        ),
    ]
