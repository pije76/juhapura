# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matrimonial', '0012_auto_20170324_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mobile_no',
        ),
    ]