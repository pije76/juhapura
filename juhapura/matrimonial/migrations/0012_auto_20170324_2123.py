# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0011_auto_20170324_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]