from django.contrib import admin

from products.models import (
    Category,
    Manufacturer,
    Product,
    StockInventory,
    StockPosition,
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(StockInventory)
admin.site.register(StockPosition)