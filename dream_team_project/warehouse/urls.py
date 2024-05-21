from django.urls import include, path
from rest_framework.routers import DefaultRouter

from warehouse.views import CustomerViewSet, EmployeeViewSet, PersonViewSet

router = DefaultRouter()
router.register(r"persons", PersonViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"employees", EmployeeViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
