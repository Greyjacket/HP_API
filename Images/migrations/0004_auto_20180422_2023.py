# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-22 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Images', '0003_auto_20180422_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='source_identifier',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]