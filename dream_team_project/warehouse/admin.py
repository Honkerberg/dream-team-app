from django.contrib import admin
from warehouse.models import Customer, Employee, Person
from warehouse.exceptions import WrongPersonException


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["person_id", "email", "ship_address"]
    ordering = ["person_id"]
    def save_model(self, request, obj, form, change) -> None:
        if obj.person_id.typ_osoba == "CUS":
            return super().save_model(request, obj, form, change)
        else:
            raise WrongPersonException(
                message=f"Wrong assignment to Customer. Type of person is {obj.person_id.typ_osoba}"
            )


admin.site.register(Customer, CustomerAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["person_id", "job_position"]
    ordering = ["person_id"]
    def save_model(self, request, obj, form, change) -> None:
        if obj.person_id.typ_osoba == "EMP":
            return super().save_model(request, obj, form, change)
        else:
            raise WrongPersonException(
                message=f"Wrong assignment to Employee. Type of person is {obj.person_id.typ_osoba}"
            )


admin.site.register(Employee, EmployeeAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "birth_date"]
    ordering = ["id"]

admin.site.register(Person, PersonAdmin)
