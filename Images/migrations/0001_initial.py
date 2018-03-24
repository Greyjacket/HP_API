# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-19 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=16, unique=True)),
                ('root_sku', models.CharField(max_length=16, unique=True)),
                ('old_sku', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(max_length=128)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('material_type', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=64)),
                ('sub_category', models.CharField(max_length=64)),
                ('collection', models.CharField(max_length=72)),
                ('sub_collection', models.CharField(max_length=72)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('path', models.CharField(blank=True, max_length=400, null=True)),
                ('variations', models.CharField(blank=True, max_length=400, null=True)),
                ('variation_group', models.CharField(blank=True, max_length=20, null=True)),
                ('info', models.CharField(blank=True, max_length=200, null=True)),
                ('validated', models.BooleanField(default=False)),
            ],
        ),
    ]
