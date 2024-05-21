from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class StockPosition(models.Model):
    rack_name = models.CharField(_("Rack Name"), max_length=20)
    shelf_name = models.CharField(_("Shelf Name"), max_length=20)

    def __str__(self) -> str:
        return f"{self.rack_name} {self.shelf_name}"


class Category(models.Model):
    category_name = models.CharField(_("Category Name"), max_length=50)
    category_description = models.TextField(_("Category Description"), max_length=200)
    stock_position_id = models.ForeignKey(StockPosition, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.category_name}"


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(_("Manufacturer"), max_length=50)
    manufacturer_country = models.CharField(_("Manufacturer Country"), max_length=20)

    def __str__(self) -> str:
        return f"{self.manufacturer_name}"


class Product(models.Model):
    product_name = models.CharField(_("Product Name"), max_length=100)
    product_price = models.DecimalField(
        _("Product Price"), max_digits=10, decimal_places=2
    )

    class Currency(models.TextChoices):
        czech = "CZK", _("Czech crowns")
        dollar = "USD", _("Dollar")
        euros = "EUR", _("Euros")

    product_currency = models.CharField(choices=Currency.choices, max_length=3)
    product_category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product_name}"
    
    @property
    def currency_converter(self):
        if self.product_currency == "CZK":
            return self.product_price
        elif self.product_currency == "USD":
            return self.product_price * 23
        elif self.product_currency == "EUR":
            return self.product_price * 24
        else:
            return self.product_price


class StockInventory(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quantity"))
    date_of_acceptance = models.DateField(_("Date of Acceptance"))
    date_of_manufacture = models.DateField(
        _("Date of Manufacture"), blank=True, null=True
    )
    expiration_date = models.DateField(_("Expiration Date"), blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.product_id}"
