from django.contrib import admin

from products.models import (
    Category,
    Manufacturer,
    Product,
    StockInventory,
    StockPosition,
)

# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["manufacturer_name", "manufacturer_country"]
admin.site.register(Manufacturer, ManufacturerAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name", "category_description", "stock_position_id"]
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_price", "product_currency", "product_manufacturer_id"]
admin.site.register(Product, ProductAdmin)


class StockInventoryAdmin(admin.ModelAdmin):
    list_display = ["product_id", "quantity", "date_of_acceptance", "date_of_manufacture", "expiration_date"]
admin.site.register(StockInventory, StockInventoryAdmin)

admin.site.register(StockPosition)