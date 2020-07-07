from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>/menu", views.menu, name = "menu"),
    path("orderPizza", views.orderPizza, name="orderPizza"),
    path("orderBurger", views.orderBurger, name="orderBurger"),
    path("addCartPizza", views.addCartPizza, name = "addCartPizza"),
    path("addCartBurger", views.addCartBurger, name = "addCartBurger"),
    path("<str:name>/viewCart", views.viewCart, name ="viewCart"),
    path("<str:name>/placeOrder", views.placeOrder, name = "placeOrder"),
    path("trackOrder", views.trackOrder, name = "trackOrder"),

    path("restaurant", views.allOrders, name = "allOrders"),
    path("restaurant/<int:order_id>/viewOrder", views.viewOrder, name = "viewOrder"),
    path("restaurant/removePizza", views.deletePizza, name = "deletePizza"),
    path("restaurant/removeBurger", views.deleteBurger, name = "deleteBurger"),
    path("restaurant/deleteOrder", views.deleteOrder, name = "deleteOrder"),
    path("restaurant/burgerToppingPage", views.burgerToppingPage, name = "burgerToppingPage"),
    path("restaurant/addBurgerTopping", views.addBurgerTopping, name = "addBurgerTopping")
]
