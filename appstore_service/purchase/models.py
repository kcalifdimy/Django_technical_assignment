import uuid

from django.db import models

from appstore_service.apps.models import App
from appstore_service.users.models import User


class Purchase(models.Model):
    """
    Purchase model
    """
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    unique_key = models.CharField(max_length=40, unique=True)

    # Override the save method to generate a unique key if one doesn't already
    # exist.
    # - Uses Python's uuid4 to create a random UUID string.
    # - The unique key is only generated when the purchase is first saved.
    def save(self, *args, **kwargs):
        if not self.unique_key:
            self.unique_key = str(uuid.uuid4())
        super().save(*args, **kwargs)
