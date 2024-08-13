from django.urls import path

from appstore_service.purchase.api import views

# Namespace for purchase-related URLs
app_name = "purchase" 

urlpatterns = [
    # URL pattern for purchasing an app by app_id
    path('apps/<int:app_id>/purchase/',
         views.PurchaseAppView.as_view(),
         name='purchase-create'),
    # URL pattern for listing all purchases
    path('list', views.PurchaseListView.as_view(),
         name='purchase-list'),
]
