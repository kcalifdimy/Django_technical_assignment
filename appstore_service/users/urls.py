"""
URL patterns for user-related API endpoints.
"""


from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from appstore_service.users.api.views import (
    SignupView, UserListView, UserRetrieveUpdateDestroyAPIViews)

# Namespace for user-related URLs
app_name = "users"
urlpatterns = [
    # URL pattern for user registration
    path('signup',
         SignupView.as_view(),
         name='signup_user'),
    # URL pattern for obtaining JWT access and refresh tokens
    path('signin/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    # URL pattern for refreshing JWT tokens
    path('signin/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    # URL pattern for listing all users
    path('list', 
         UserListView.as_view(),
         name='user-list'),
    # URL pattern for retrieving, updating, or deleting a specific user by
    # primary key (pk)
    path('details/<int:pk>',
         UserRetrieveUpdateDestroyAPIViews.as_view(),
         name='user-details'),
]
