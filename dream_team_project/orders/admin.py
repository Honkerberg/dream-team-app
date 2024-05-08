from django.contrib import admin

from orders.models import Order, OrderLines, Shipping

# Register your models here.
admin.site.register(Order)
admin.site.register(Shipping)
admin.site.register(OrderLines)