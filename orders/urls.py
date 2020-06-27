from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orderPizza", views.orderPizza, name="orderPizza"),
    path("addCartPizza", views.addCartPizza, name = "addCartPizza"),
    path("<str:name>/viewCart", views.viewCart, name ="viewCart")
]
