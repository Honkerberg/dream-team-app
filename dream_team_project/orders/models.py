from django.db import models
from django.utils.translation import gettext_lazy as _
from warehouse.models import Customer, Employee
from products.models import Product


# Create your models here.
class Shipping(models.Model):
    shipment_name = models.CharField(_("Shipment"), max_length=100)
    shipment_price = models.DecimalField(
        _("Shipment Price"),
        max_digits=10,
        decimal_places=2
    )

    def __str__(self) -> str:
        return f"{self.shipment_name}"


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipment_id = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id}" # type: ignore


class OrderLines(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

