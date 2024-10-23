from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=30, verbose_name='телефон')
    country = models.CharField(max_length=50, verbose_name='страна')
    avatar = models.ImageField(upload_to="avatar/", verbose_name="аватар", **NULLABLE)

    token = models.CharField(max_length=100, verbose_name='Token', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
