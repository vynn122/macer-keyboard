from django.test import TestCase
from keyboardApp.models import User_info, Store_item, Transaction

class TransactionTest(TestCase):
    databases = {"default", "keyboardAppDB"}

    def test_create_transaction(self):
        user = User_info.objects.create(
            user_name="john",
            user_nickname="John",
            user_password="123"
        )

        product = Store_item.objects.create(
            item_name="Keyboard X",
            item_price=100
        )

        transaction = Transaction.objects.create(
            transaction_user=user,
            item=product
        )

        self.assertEqual(transaction.reviewed_flag, 0)