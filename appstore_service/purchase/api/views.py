from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from appstore_service.apps.models import App
from appstore_service.purchase.api.permissions import IsOwnerOrReadOnly
from appstore_service.purchase.api.serializers import PurchaseSerializer
from appstore_service.purchase.models import Purchase


class PurchaseAppView(APIView):
    """
    View for handling the purchase of an app.
    Inherits from APIView to handle POST requests for purchasing apps.
    Only authenticated users can access this view.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, app_id=None, format=None):
        # Fetch the app based on the provided app_id.
        # - Uses get_object_or_404 to return a 404 error if the app does not
        # exist.
        app = get_object_or_404(App, id=app_id)
        # Fetch the current authenticated user.
        user = request.user
        # Check if the user has already purchased this app.
        # - If the purchase already exists, return a 400 Bad Request response
        # with an error message.
        if Purchase.objects.filter(buyer_id=user.id, app=app).exists():
            return Response({"error": "You have already purchased this app"},
                            status=status.HTTP_400_BAD_REQUEST
                            )

        # Check if the user has sufficient funds to purchase the app.
        # - If the user's balance is less than the app price, return a 400 Bad
        # Request response with an error message.
        if user.credit < app.price:
            return Response({"error": "Insufficient balance"},
                            status=status.HTTP_400_BAD_REQUEST
                            )

        # Deduct the app price from the user's balance and save the updated
        # balance.
        user.credit -= app.price
        user.save()
        # Create a context dictionary to pass the request object to the
        # serializer.
        serializer_context = {
            'request': request,
        }
        # Create a new Purchase instance for the app and save it to the
        # database.
        purchase = Purchase(buyer=user, app=app)
        purchase.save()

        # Serialize the purchase data using the PurchaseSerializer.
        serializer = PurchaseSerializer(purchase, context=serializer_context)
        # Return the serialized purchase data in the response with a 201
        # Created status.
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PurchaseListView(generics.ListAPIView):
    """
    View for listing all purchases.Inherits from ListAPIView to provide 
    a read-only list of Purchase instances.
    Uses the PurchaseSerializer to serialize the data.
    The IsOwnerOrReadOnly permission ensures that users can only see their
    own purchases.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsOwnerOrReadOnly]
