# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-28 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurantlocation_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
