from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# router.register('api/vendor' , views.VendorView)
# router.register('api/vendor/<int:pk>' , views.VendorViewUpdate)

urlpatterns = [
    path('GET/api/vendor/' , views.VendorView.as_view(),name="vendorPost"),
    path('POST/api/vendor/' , views.VendorViewPost.as_view(),name="vendorGet"),
    path('GET/api/vendors/<int:id>/' , views.VendorRetriving.as_view(),name="vendorRet"),
    path('PUT/api/vendors/<int:id>/' , views.VendorUpdate.as_view(),name="vendorUpdate"),
    path('DELETE/api/vendors/<int:id>/' , views.DeleteVendor.as_view(),name="vendorDel"),
]