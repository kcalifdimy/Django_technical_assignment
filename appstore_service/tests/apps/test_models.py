import pytest

pytestmark = pytest.mark.django_db


class TestAppModels:
    def test_str_method(self, app_factory):
        obj = app_factory()
        assert obj.__str__() == "machine"
        