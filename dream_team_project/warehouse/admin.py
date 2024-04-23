from django.contrib import admin
from warehouse.models import Customer, Employee, Person


class CustomerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        if obj.person_id.typ_osoba == "CUS":
            return super().save_model(request, obj, form, change)
        else:
            raise ValueError


admin.site.register(Customer, CustomerAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) -> None:
        if obj.person_id.typ_osoba == "EMP":
            return super().save_model(request, obj, form, change)
        else:
            raise ValueError


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Person)
