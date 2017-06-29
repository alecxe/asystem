# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20170626_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Auction end date'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='auction_start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Auction start date'),
        ),
    ]