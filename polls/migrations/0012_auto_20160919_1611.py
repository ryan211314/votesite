# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 08:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20160919_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='person',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
