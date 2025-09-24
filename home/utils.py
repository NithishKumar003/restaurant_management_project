import string
import secrets
from .models import Coupon  # make sure you have a Coupon model


def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    :param length: Length of the coupon code (default=10)
    :return: Unique coupon code string
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        # Generate random code
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Ensure uniqueness by checking DB
        if not Coupon.objects.filter(code=code).exists():
            return code
