# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20170626_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioneer',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]