# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeesList', '0002_auto_20161116_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='end_work',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Окончание работы'),
        ),
    ]
