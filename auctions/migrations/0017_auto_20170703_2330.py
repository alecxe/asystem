# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-03 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20170703_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempicture',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itempicture',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
