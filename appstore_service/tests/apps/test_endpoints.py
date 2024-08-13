from django.urls import resolve, reverse

from appstore_service.apps.models import App


class TestAppEndpoint:
    def test_user_detail(self, app: App):
        assert (
            reverse("apps:app-detail", kwargs={"pk":app.pk}) == f"/api/apps/details/{app.pk}/"
        )
        assert resolve(f"/api/apps/details/{app.pk}/").view_name == "apps:app-detail"

    def test_app_list(self):
        assert reverse("apps:app-list") == "/api/apps/list"
        assert resolve("/api/apps/list").view_name == "apps:app-list"
        