# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20170702_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_categories',
            field=models.ManyToManyField(related_name='items', to='auctions.ItemCategory'),
        ),
    ]