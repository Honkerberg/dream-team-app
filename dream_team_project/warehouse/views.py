from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from warehouse.models import Person, Customer, Employee
from warehouse.serializers import PersonSerializer, CustomerSerializer, EmployeeSerializer


# Create your views here.

class TeamView(GenericAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "warehouse/team.html"

    def get(self, request):
        return Response(template_name=self.template_name)
    
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "warehouse/persons.html"

    def get_object(self):
        return super().get_object()
    
    def list(self, request):
        return Response({"persons": self.queryset}, template_name=self.template_name)
    
    def retrieve(self, request, *args, **kwargs):
        return Response({"person": self.get_object()}, template_name=self.template_name)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
