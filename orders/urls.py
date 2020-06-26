from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orderPizza", views.orderPizza, name="orderPizza"),
    path("placePizzaOrder", views.placePizzaOrder, name = "placePizzaOrder")
]
