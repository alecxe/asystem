# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0034_auctioneer_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioneer',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auctioneer_address', to='auctions.Address', verbose_name='Address'),
        ),
    ]