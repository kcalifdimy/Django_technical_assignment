from rest_framework import permissions, status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response

from appstore_service.users.api.permissions import IsOwnerOrReadOnly
from appstore_service.users.api.serializers import UserSerializer
from appstore_service.users.models import User


class SignupView(CreateAPIView):
    """
    View for user registration (signup).
    Allows any user to register (permission_classes set to AllowAny).
    Uses UserSerializer to validate and save user data.
    """
    # Allow any user to access this view
    permission_classes = [permissions.AllowAny]
    # Serializer used for validating and creating user data
    serializer_class = UserSerializer
 
    def post(self, request):
        # Initialize serializer with request data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Save new user if data is valid
            serializer.save()
            response = {
                'success': 'True',
                # Success message on successful registration
                'message': 'User registered successfully',
            }
            # Return success response with HTTP 201 Created status
            return Response(response, status=status.HTTP_201_CREATED)
        # Return error response with HTTP 400 Bad Request status if data is
        # invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(ListAPIView):
    """
    View for listing all users.
    Retrieves and displays a list of all User instances using UserSerializer.
     """
    permission_classes = [permissions.IsAuthenticated]
    # require authentication for accessing this view
    # Retrieve all User instances
    queryset = User.objects.all()
    # Serializer used for displaying user data
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIViews(RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting a specific user.
    Requires authentication and checks if the user is the owner or
    #has read-only access.
    """
    # Retrieve all User instances
    queryset = User.objects.all()
    # Permissions for authenticated or read-only access, and ownership
    # validation
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    # Serializer used for retrieving, updating, or deleting user data
    serializer_class = UserSerializer
