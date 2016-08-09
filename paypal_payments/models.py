from __future__ import unicode_literals

from django.db import models


class RecurringSubscription(models.Model):
    user = models.ForeignKey('auth.User', null=True, blank=True)
    recurring_payment_id = models.CharField(
        max_length=25, db_index=True, unique=True)
    initial_payment_amount = models.DecimalField(
        max_digits=7, decimal_places=2)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=7, decimal_places=2)
    shipping = models.DecimalField(max_digits=7, decimal_places=2)
    outstanding_balance = models.DecimalField(max_digits=7, decimal_places=2)
    amount_per_cycle = models.DecimalField(max_digits=7, decimal_places=2)
    payment_cycle = models.CharField(max_length=25)
    product_name = models.CharField(max_length=125)
    product_type = models.CharField(max_length=5)
    charset = models.CharField(max_length=15)
    currency_code = models.CharField(max_length=5)
    custom = models.CharField(null=True, blank=True, max_length=255)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    payer_email = models.EmailField(max_length=255)
    receiver_email = models.EmailField(max_length=255)
    history = models.TextField()
    time_created = models.DateTimeField()
    txn_type = models.CharField(max_length=250)
    verify_sign = models.CharField(max_length=250)
    profile_status = models.CharField(max_length=25, db_index=True)
    notify_version = models.CharField(null=True, blank=True, max_length=10)
    ipn_track_id = models.CharField(null=True, blank=True, max_length=20, db_index=True)
