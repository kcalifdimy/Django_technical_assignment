from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "appstore_service.users"
    label = "users"

    def ready(self):
        from . import signals  # noqa
