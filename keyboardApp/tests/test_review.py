from django.test import TestCase
from keyboardApp.models import User_info, Store_item, Reviews

class ReviewTest(TestCase):
    databases = {"default", "keyboardAppDB"}

    def test_create_review(self):
        user = User_info.objects.create(
            user_name="reviewer",
            user_nickname="Reviewer",
            user_password="123"
        )

        product = Store_item.objects.create(
            item_name="Keyboard Review",
            item_price=50
        )

        review = Reviews.objects.create(
            user_id=user,
            store_item_id=product,
            rating=5,
            review_text="Excellent keyboard"
        )

        self.assertEqual(review.rating, 5)