from collections.abc import Sequence
from typing import Any

import factory
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from appstore_service.apps.models import App
from appstore_service.users.models import User


class UserFactory(DjangoModelFactory):
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    @classmethod
    def _after_postgeneration(cls, instance, create, results=None):
        """Save again the instance if creating and at least one hook ran."""
        if create and results and not cls._meta.skip_postgeneration_save:
            # Some post-generation hooks ran, and may have modified us.
            instance.save()

    class Meta:
        model = User
        django_get_or_create = ["email"]


class AppFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = App  
    id = 1   
    owner = factory.SubFactory(UserFactory)
    title = "machine"
    description = " Its an app for machine"
    price = 4.00
    verified = True
    created_at = "2024-08-12T14:30:43.339695Z"
    icon = ""




