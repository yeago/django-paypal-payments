# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payments', '0002_recurringsubscription_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurringsubscription',
            name='receiver_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recurringsubscription',
            name='subscr_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='recurringsubscription',
            name='txn_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='recurringsubscription',
            name='recurring_payment_id',
            field=models.CharField(blank=True, db_index=True, max_length=25, null=True, unique=True),
        ),
    ]
