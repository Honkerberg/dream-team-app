from rest_framework import serializers
from orders.models import Order, OrderLines, Shipping



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderLinesSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product_id.product_name")
    product_price = serializers.CharField(source="product_id.currency_converter")
    total_price = serializers.CharField(source="get_total_price")
    class Meta:
        model = OrderLines
        fields = ("id", "order_id", "product_name", "quantity", "product_price", "total_price")


class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = "__all__"
