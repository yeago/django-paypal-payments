# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-11 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal_payments', '0003_auto_20160810_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurringsubscription',
            name='initial_payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='recurringsubscription',
            name='outstanding_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
