# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]
