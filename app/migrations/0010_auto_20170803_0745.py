# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-08-03 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170803_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbankdata',
            name='Address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bloodbankdata',
            name='Contact',
            field=models.TextField(),
        ),
    ]
