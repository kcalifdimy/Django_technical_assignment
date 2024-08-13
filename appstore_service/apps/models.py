from decimal import Decimal

from django.conf import settings
from django.db import models


# App models here
class App(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    title = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to='icons/%Y/%m/%d/',
        blank=True, null=True
    )
    description = models.TextField()
    verified = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
