# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-03 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170802_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbankdata',
            name='Address',
            field=models.CharField(max_length=100),
        ),
    ]
