from django.db import models
import uuid

# Create your models here.
class Vendor (models.Model):
    unique_vendor_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=220)
    address=models.TextField(max_length=250)

    def __str__(self):
        return f'{self.name} with id {self.unique_vendor_code}'
