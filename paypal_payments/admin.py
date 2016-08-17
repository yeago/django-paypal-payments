from django.contrib import admin

from paypal_payments.models import RecurringSubscription


class RecurringAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ['user', 'last_update', 'profile_status', 'txn_id', 'txn_type']


admin.site.register(RecurringSubscription, RecurringAdmin)
