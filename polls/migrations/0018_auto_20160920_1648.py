# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20160920_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='pgrade', to='polls.GradeQuestion'),
        ),
    ]