from __future__ import unicode_literals
from dateutil import parser
from django.db import models


class RecurringSubscription(models.Model):
    user = models.ForeignKey('auth.User', null=True, blank=True)
    recurring_payment_id = models.CharField(
        max_length=25, db_index=True, unique=True, null=True, blank=True)
    initial_payment_amount = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    shipping = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    outstanding_balance = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    amount_per_cycle = models.DecimalField(
        null=True, blank=True, max_digits=7, decimal_places=2)
    payment_cycle = models.CharField(
        null=True, blank=True, max_length=25)
    product_name = models.CharField(max_length=125)
    product_type = models.CharField(max_length=5)
    charset = models.CharField(max_length=15)
    currency_code = models.CharField(max_length=5)
    custom = models.CharField(null=True, blank=True, max_length=255)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    payer_email = models.EmailField(max_length=255)
    receiver_email = models.EmailField(max_length=255)
    receiver_id = models.CharField(max_length=255, null=True, blank=True)
    history = models.TextField(null=True, blank=True)
    time_created = models.DateTimeField()
    txn_id = models.CharField(max_length=250, null=True, blank=True)
    subscr_id = models.CharField(max_length=250, null=True, blank=True)
    txn_type = models.CharField(max_length=250)
    verify_sign = models.CharField(max_length=250)
    profile_status = models.CharField(max_length=25, db_index=True)
    notify_version = models.CharField(null=True, blank=True, max_length=10)
    ipn_track_id = models.CharField(
        null=True, blank=True, max_length=20, db_index=True)
    last_update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.time_created and type(self.time_created) in [unicode, str]:
            self.time_created = parser.parse(self.time_created)
        if self.pk:
            orig = RecurringSubscription.objects.get(pk=self.pk)
            changed = []
            for field, value in sorted(orig.__dict__.items(), key=lambda x: x[0], reverse=True):
                if field in ["_state", "history"]:
                    continue
                if getattr(self, field, None) != value:
                    changed.append((field, value))
            if changed:
                self.history = self.history or ""
                if self.history:
                    self.history = "================\n%s" % self.history
                for (field, val) in changed:
                    if self.history:
                        self.history = "\n%s" % self.history
                    self.history = "%s  ->  %s%s" % (field, val, self.history)
        super(RecurringSubscription, self).save(*args, **kwargs)
