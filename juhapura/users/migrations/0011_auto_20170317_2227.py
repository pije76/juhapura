# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170317_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='looking_for',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='reason_registration',
            field=models.IntegerField(choices=[(1, "I'm registring to find myself a partner"), (2, "I'm registring to find my friend a partner"), (3, "I'm registring to find my son a partner"), (4, "I'm registring to find my daughter a partner"), (5, "I'm registring to find my brother a partner"), (6, "I'm registring to find my sister a partner")], null=True),
        ),
    ]
