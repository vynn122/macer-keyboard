from django.test import TestCase
from keyboardApp.models import User_info

class UserTest(TestCase):
    databases = {"default", "keyboardAppDB"}

    def test_create_user(self):
        user = User_info.objects.create(
            user_name="vynn",
            user_nickname="Vynn",
            user_password="123456"
        )

        self.assertEqual(user.user_name, "vynn")

    def test_default_role(self):
        user = User_info.objects.create(
            user_name="admin", 
            user_nickname="Admin",
            user_password="123456"
        )

        self.assertEqual(user.user_role, "user")