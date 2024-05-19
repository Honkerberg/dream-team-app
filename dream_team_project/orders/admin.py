from django.contrib import admin

from orders.models import Order, OrderLines, Shipping


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_id", "shipment_id", "employee_id"]
    ordering = ["customer_id"]


admin.site.register(Order, OrderAdmin)


class OrderLinesAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "product_id", "quantity"]
    ordering = ["id"]


admin.site.register(OrderLines, OrderLinesAdmin)


class ShippingAdmin(admin.ModelAdmin):
    list_display = ["shipment_name", "shipment_price"]
    ordering = ["shipment_name"]


admin.site.register(Shipping, ShippingAdmin)
