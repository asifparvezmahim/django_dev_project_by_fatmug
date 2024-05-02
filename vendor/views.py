from django.shortcuts import render
from . models import Vendor
from rest_framework import viewsets
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.views import APIView
# Create your views here.
class VendorViewPost(APIView):
    def get (self,request):
        vendor = Vendor.objects.all()
        serializer = serializers.VendorSerializer(vendor,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

    def post (self,request):
        serializer=serializers.VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class VendorView(APIView):
    def get (self,request):
        vendor = Vendor.objects.all()
        serializer = serializers.VendorSerializer(vendor,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)

class VendorUpdate(APIView):
    def get (self,request,id):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg={"NOT FOUND ERROR"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=serializers.VendorSerializer(vendor)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def put (self,request,id):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg={"NOT FOUND ERROR"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer=serializers.VendorSerializer(vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class VendorRetriving(APIView):
    def get (self,request,id):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg={"NOT FOUND ERROR"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=serializers.VendorSerializer(vendor)
        return Response (serializer.data,status=status.HTTP_200_OK)

class DeleteVendor(APIView):
    def get (self,request,id):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg={"NOT FOUND ERROR"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer=serializers.VendorSerializer(vendor)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        try:
            vendor = Vendor.objects.get(id=id)
        except Vendor.DoesNotExist:
            msg={"NOT FOUND ERROR"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        vendor.delete()
        return Response({"msg":"Deleted"},status=status.HTTP_204_NO_CONTENT)


