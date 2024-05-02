from django.db import models
import uuid
from vendor.models import Vendor

# Create your models here.
class OrderTracking (models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    product_order_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)
    delivery_date=models.DateField()
    items = models.JSONField(default={"product_name": ""})
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=40, choices=ORDER_STATUS_CHOICES, default='pending')
    quality_rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.vendor.name



