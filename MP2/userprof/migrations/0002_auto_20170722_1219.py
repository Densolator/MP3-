# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 04:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprof', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]