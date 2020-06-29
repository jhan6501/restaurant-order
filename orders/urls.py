from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/menu", views.menu, name = "menu"),
    path("orderPizza", views.orderPizza, name="orderPizza"),
    path("addCartPizza", views.addCartPizza, name = "addCartPizza"),
    path("<str:name>/viewCart", views.viewCart, name ="viewCart"),
    path("<str:name>/placeOrder", views.placeOrder, name = "placeOrder")
    #path("viewCart", views.viewCart, name = "viewCart")
]
