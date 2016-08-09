from django.test import TestCase
from paypal_payments.models import RecurringSubscription


class RecurringPaymentTestCase(TestCase):
    def test_history(self):
        instance = RecurringSubscription.objects.create(
            recurring_payment_id="blah",
            initial_payment_amount=2.99,
            amount=2.99,
            tax=2.99,
            shipping=2.99,
            outstanding_balance=0,
            amount_per_cycle=2.99,
            payment_cycle=2.99,
            product_name="blah",
            product_type="blah",
            charset="blah",
            currency_code="blah",
            custom="blah",
            first_name="blah",
            last_name="blah",
            payer_email="blah@blah.com",
            receiver_email="blah@blah.com",
            time_created="06:19:40 Feb 29, 2016 PST",
            txn_type="blah",
            verify_sign="blah",
            profile_status="blah",
            notify_version="blah",
            ipn_track_id="blah",
        )
        last_update = str(instance.last_update).split(".")[0]
        instance = RecurringSubscription.objects.get(
            recurring_payment_id="blah")
        instance.first_name = "blah2"
        instance.profile_status = "blah2"
        instance.save()
        self.assertEqual(
            instance.history,
            u"first_name  ->  blah\nprofile_status  ->  blah")
        last_update2 = str(instance.last_update).split(".")[0]
        instance.first_name = "blah3"
        instance.profile_status = "blah3"
        instance.save()
        self.assertEqual(
            instance.history,
            u"first_name  ->  blah2\nlast_update  ->  %s\nprofile_status  ->  blah2\n================\nfirst_name  ->  blah\nprofile_status  ->  blah" % (last_update2))
