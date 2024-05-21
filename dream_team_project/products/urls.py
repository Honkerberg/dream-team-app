from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import CategoryViewSet, ManufacturerViewSet, StockInventoryViewSet, StockPositionViewSet, ProductListView

router = DefaultRouter()
# router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"manufacturers", ManufacturerViewSet)
router.register(r"stock_inventory", StockInventoryViewSet)
router.register(r"stock_positions", StockPositionViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("all-products/", ProductListView.as_view(), name="prod"),
    
]