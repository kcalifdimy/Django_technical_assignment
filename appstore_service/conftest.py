import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from appstore_service.tests.factories import AppFactory, UserFactory
from appstore_service.users.models import User

register(AppFactory)
register(UserFactory)


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()


@pytest.fixture()
def api_client():
    return APIClient
