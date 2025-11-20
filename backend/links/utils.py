import re
import string
import random
from urllib.parse import urlparse


def generate_short_code(length=6):
    """Generate a random alphanumeric short code of given length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def validate_url(url):
    """Validate if the URL is valid."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def validate_code(code):
    """Validate code matches [A-Za-z0-9]{6,8}"""
    return bool(re.match(r'^[A-Za-z0-9]{6,8}$', code))