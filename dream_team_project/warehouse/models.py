from composite_field import CompositeField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Address(CompositeField):
    street = models.CharField(_("Street"), max_length=50)
    number = models.IntegerField(_("Number"))
    city = models.CharField(_("City"), max_length=40)
    postal_code = models.CharField(_("Postal code"), max_length=6)

    def get_proxy(self, model):
        return super().get_proxy(model)

    class Proxy(CompositeField.Proxy):
        def __repr__(self):
            return f"{self.street} {self.number}, {self.city}"


class ShipAddress(CompositeField):
    street = models.CharField(_("Ship address"), max_length=50, blank=True)
    number = models.IntegerField(_("Number"), blank=True)
    city = models.CharField(_("City"), max_length=40, blank=True)
    postal_code = models.CharField(_("Postal code"), max_length=6, blank=True)

    def get_proxy(self, model):
        return super().get_proxy(model)

    class Proxy(CompositeField.Proxy):
        def __repr__(self):
            return f"{self.street} {self.number}, {self.postal_code}, {self.city}"


class Person(models.Model):
    class PersonChoices(models.TextChoices):
        ## Insert type of persons
        employee = "EMP", _("Employee")
        customer = "CUS", _("Customer")

    typ_osoba = models.CharField(
        choices=PersonChoices.choices,
        max_length=3,
    )
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    birth_date = models.DateField(_("Birth date"))
    address = Address(_("Address"))
    phone_number = models.CharField(_("Phone"), max_length=20)

    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - (self.birth_date.year)
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")


class Customer(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)
    email = models.EmailField(_("Email"))
    ship_address = ShipAddress(_("Ship address"))

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self) -> str:
        return f"{self.person_id}"


class Employee(models.Model):
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE)

    class EmployeePosition(models.TextChoices):
        manager = "MAN", _("Manager")
        accountant = "ACC", _("Accountant")
        technician = "TEC", _("Technician")
        warehouseman = "WHM", _("Warehouseman")

    job_position = models.CharField(
        _("Job position"),
        choices=EmployeePosition.choices,
        max_length=3,
    )

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self) -> str:
        return f"{self.person_id}"
