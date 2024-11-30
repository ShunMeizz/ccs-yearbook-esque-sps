from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
from datetime import timedelta
import six

class ProfileTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_acc_verified))
    
profile_token = ProfileTokenGenerator()

class CustomPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def __init__(self, timeout_seconds=180):
        self.timeout = timedelta(seconds=timeout_seconds)
        super().__init__()

    def _make_hash_value(self, user, timestamp):
        return f'{user.pk}{user.password}{timestamp}'

    def check_token(self, user, token):
        try:
            # Check the token's expiration time
            if timezone.now() - token.created > self.timeout:
                return False
            return super().check_token(user, token)
        except Exception:
            return False