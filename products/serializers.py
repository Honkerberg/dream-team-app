from rest_framework import serializers
from products.models import Product, Category, Manufacturer, StockInventory, StockPosition


class ProductSerializer(serializers.ModelSerializer):
    manufacturer_id = serializers.CharField(source="product_manufacturer_id.manufacturer_name")
    class Meta:
        model = Product
        fields = ("id", "product_name", "product_price", "manufacturer_id", "product_currency")

    def get_new_price(self, obj):
        return obj.currency_converter

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"

class StockInventorySerializer(serializers.ModelSerializer):        
    class Meta:
        model = StockInventory
        fields = "__all__"

class StockPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPosition
        fields = "__all__"