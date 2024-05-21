from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet, OrderLinesViewSet, ShippingViewSet


router = DefaultRouter()
router.register(r"orders", OrderViewSet)
router.register(r"order_lines", OrderLinesViewSet)
router.register(r"shipping", ShippingViewSet)


urlpatterns = [
    path("", include(router.urls)),
]