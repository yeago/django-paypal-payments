# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-09 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurringsubscription',
            name='last_update',
            field=models.DateTimeField(auto_now=True, default=None),
            preserve_default=False,
        ),
    ]
