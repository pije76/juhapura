# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170316_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(blank=True, max_length=255, verbose_name='Name of User'),
        ),
    ]
