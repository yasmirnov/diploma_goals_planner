from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    REQUIRED_FIELDS = []


class UserAb(AbstractUser):
    pass
