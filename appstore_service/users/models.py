from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Custom user model for appstore_service.
    """
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    email = models.EmailField(_("email address"), unique=True)
    credit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=100.00
    )
    username = None  # type: ignore[assignment]

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects: ClassVar[UserManager] = UserManager()
