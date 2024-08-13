
from django.contrib import admin

from appstore_service.purchase.models import Purchase


class PurchaseAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Purchase model.
    This class customizes how Purchase instances are displayed and managed 
    in the Django admin panel.
    """

    # Fields to be displayed in the list view of the admin panel.
    # - 'buyer': The user who purchased the app.
    # - 'app': The app that was purchased.
    # - 'purchase_date': The date when the purchase was made.
    # - 'unique_key': A unique key associated with the purchase.
    list_display = (
        'buyer',
        'app',
        'purchase_date',
        'unique_key',
    )
    # Allows inline editing of the 'purchase_date'
    list_editable = (
        'unique_key',
    )
    # Override the default queryset to order the Purchase instances by the
    # associated app.
    
    def get_queryset(self, request):
        queryset = super(PurchaseAdmin, self).get_queryset(request)
        queryset = queryset.order_by('app')
        return queryset


# Register the Purchase model with the custom PurchaseAdmin configuration
admin.site.register(Purchase, PurchaseAdmin)
