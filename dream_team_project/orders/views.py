from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from orders.models import Order, OrderLines, Shipping
from orders.serializers import OrderSerializer, OrderLinesSerializer, ShippingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "orders/orders.html"

    def get_queryset(self):
        return Order.objects.all()

    def list(self, request, *args, **kwargs):
        return Response({"orders": self.get_queryset}, template_name=self.template_name)

    def retrieve(self, request, pk=None):
        queryset = OrderLines.objects.filter(order_id=pk)
        # category = get_object_or_404(queryset)
        serializer = OrderLinesSerializer(queryset, many=True)
        template_name = "orders/order_detail.html"
        return Response({"data": serializer.data}, template_name=template_name)

class OrderLinesViewSet(viewsets.ModelViewSet):
    queryset = OrderLines.objects.all()
    serializer_class = OrderLinesSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "orders/order_detail.html"


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
