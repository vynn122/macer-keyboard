from django.test import TestCase
from keyboardApp.models import Store_item

class ProductTest(TestCase):
    databases = {"default", "keyboardAppDB"}

    def test_create_product(self):
        product = Store_item.objects.create(
            item_name="Akko 5075B",
            item_price=99.99,
            item_description="Mechanical Keyboard",
            item_key_color="Black",
            item_brand="Akko"
        )

        self.assertEqual(product.item_name, "Akko 5075B")

def test_product_brand(self):
    product = Store_item.objects.create(
        item_name="Akko Black",
        item_price=150,
        item_brand="Akko"
    )

    self.assertEqual(product.item_brand, "Akko")