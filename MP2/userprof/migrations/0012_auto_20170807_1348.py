# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0011_auto_20170807_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_condition',
            field=models.CharField(choices=[('USED', 'Used'), ('Brand New', 'Brand New')], default='BNEW', max_length=20),
        ),
    ]
