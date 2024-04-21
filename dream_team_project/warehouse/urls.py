from django.urls import path

from warehouse import views


urlpatterns = [
    path("", views.index, name="index")
]
