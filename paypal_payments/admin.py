from django.contrib import admin

from paypal_payments.models import SubscriptionProfile, SubscriptionTxn


class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']
    list_display = ['user', 'last_update', 'profile_status']


admin.site.register(SubscriptionProfile, ProfileAdmin)

admin.site.register(SubscriptionTxn, ProfileAdmin)
