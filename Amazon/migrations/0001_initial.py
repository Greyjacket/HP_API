# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-19 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amazon_Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_sku', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=200)),
                ('asin', models.CharField(blank=True, max_length=64, null=True)),
                ('catalog_number', models.CharField(blank=True, max_length=200, null=True)),
                ('part_number', models.CharField(blank=True, max_length=200, null=True)),
                ('size_name', models.CharField(blank=True, max_length=200, null=True)),
                ('variation_theme', models.CharField(blank=True, max_length=200, null=True)),
                ('product_tax_code', models.CharField(blank=True, max_length=200, null=True)),
                ('currency', models.CharField(blank=True, max_length=16, null=True)),
                ('is_parent', models.BooleanField()),
                ('bullet1', models.CharField(blank=True, max_length=200, null=True)),
                ('bullet2', models.CharField(blank=True, max_length=200, null=True)),
                ('bullet3', models.CharField(blank=True, max_length=200, null=True)),
                ('bullet4', models.CharField(blank=True, max_length=200, null=True)),
                ('bullet5', models.CharField(blank=True, max_length=200, null=True)),
                ('keywords', models.CharField(blank=True, max_length=20000, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sales', models.IntegerField(default=0)),
                ('parent_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Images.Image')),
            ],
        ),
        migrations.CreateModel(
            name='BulletPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('bullet', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Verification_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_verfied', models.BooleanField()),
                ('bullets_verified', models.BooleanField()),
                ('price_verified', models.BooleanField()),
                ('keywords_verified', models.BooleanField()),
                ('sku', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Amazon.Amazon_Variation')),
            ],
        ),
    ]
