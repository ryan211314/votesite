# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160918_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='person',
            field=models.ManyToManyField(to='polls.Person'),
        ),
    ]