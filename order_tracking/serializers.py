from rest_framework import serializers
from .models import OrderTracking

class VendorSerializer(serializers.ModelSerializer):
    vendor=serializers.StringRelatedField(many=False)
    class Meta:
        model = OrderTracking
        fields = "__all__"





