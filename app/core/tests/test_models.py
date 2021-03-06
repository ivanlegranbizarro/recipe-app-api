from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email(self):
        """Test creating a new user with an email"""
        email = 'test@example.com'
        password = 'testtest'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that new_user_email is normalized"""
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_user(email, 'test12334')

        self.assertEqual(user.email, email.lower())

    def test_new_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test12334')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test12334'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
