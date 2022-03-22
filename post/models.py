import string as str
from random import choice

from django.db import models
from django.urls import reverse
# from django.utils.encoding import python_2_unicode_compatible

from account.models import User


def generate_id():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))
