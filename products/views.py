from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from products.models import (
    Category,
    Manufacturer,
    Product,
    StockInventory,
    StockPosition,
)
from products.serializers import (
    CategorySerializer,
    ManufacturerSerializer,
    ProductSerializer,
    StockInventorySerializer,
    StockPositionSerializer,
)


class HomeView(GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products/base.html"

    def get(self, request):
        return Response(template_name=self.template_name)


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products/products.html"

    def get_queryset(self):
        return Product.objects.all()
    
    def get(self, request):
        self.object = self.get_queryset()
        serializer = self.get_serializer(self.object, many=True)
        return Response({"products": serializer.data}, template_name=self.template_name)
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products/categories.html"

    def get_queryset(self):
        return super().get_queryset()
    
    def list(self, request):
        return Response({"categories": self.get_queryset}, template_name=self.template_name)
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(product_category_id=pk)
        # category = get_object_or_404(queryset)
        serializer = ProductSerializer(queryset, many=True)
        template_name = "products/category_detail.html"
        return Response({"data": serializer.data}, template_name=template_name)


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "products/category_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = get_object_or_404(self.get_queryset(), pk=kwargs.get("pk"))
        serializer = self.get_serializer(self.object)
        return Response({"category_detail": serializer.data, "pk": 1}, template_name=self.template_name)
    

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    renderer_classes = [TemplateHTMLRenderer]


class StockInventoryViewSet(viewsets.ModelViewSet):
    queryset = StockInventory.objects.all()
    serializer_class = StockInventorySerializer
    renderer_classes = [TemplateHTMLRenderer]


class StockPositionViewSet(viewsets.ModelViewSet):
    queryset = StockPosition.objects.all()
    serializer_class = StockPositionSerializer
    renderer_classes = [TemplateHTMLRenderer]
