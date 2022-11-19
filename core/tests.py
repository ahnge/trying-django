import os
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password


class ConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
        try:
            is_strong = validate_password(SECRET_KEY)
            print(is_strong)
        except Exception as e:
            msg = f"Weak password - {e.messages}"
            self.fail(msg)
