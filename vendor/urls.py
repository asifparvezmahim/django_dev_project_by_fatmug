from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from order_tracking.views import OrderTrackingView,OrderPostView,OrderRetriving,OrderUpdate,DeleteOrder

router = DefaultRouter()

# router.register('api/vendor' , views.VendorView)
# router.register('api/vendor/<int:pk>' , views.VendorViewUpdate)

urlpatterns = [
    # Vendor Urls
    path('GET/api/vendor/' , views.VendorView.as_view(),name="vendorPost"),
    path('POST/api/vendor/' , views.VendorViewPost.as_view(),name="vendorGet"),
    path('GET/api/vendors/<int:id>/' , views.VendorRetriving.as_view(),name="vendorRet"),
    path('PUT/api/vendors/<int:id>/' , views.VendorUpdate.as_view(),name="vendorUpdate"),
    path('DELETE/api/vendors/<int:id>/' , views.DeleteVendor.as_view(),name="vendorDel"),

    # Order Tracking
    path('GET/api/purchase_orders/' , OrderTrackingView.as_view(),name="orderGet"),
    path('POST/api/purchase_orders/' ,OrderPostView.as_view(),name="orderPost"),
    path('GET/api/purchase_orders/<int:id>/' , OrderRetriving.as_view(),name="orderRet"),
    path('PUT/api/purchase_orders/<int:id>/' ,OrderUpdate.as_view(),name="orderUpdate"),
    path('DELETE/api/purchase_orders/<int:id>/' ,DeleteOrder.as_view(),name="orderDel"),
]