from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

orders = {}

def index(request):
    return render(request, "orders/menu.html")

def orderPizza(request):
    name = request.POST['user']
    print ("name is :" + name)
    foodItem = "Pizza"
    sizes = ["small", "large"]
    types = ["regular", "sicilian"]
    context = {
        "name": name,
        "food": foodItem,
        "sizes": sizes,
        "types": types,
    }

    return render(request, "orders/orderPizza.html", context)

def addCartPizza(request):
    name = request.POST['user']
    size = request.POST['size']
    style = request.POST['Type']
    price = 0.0
    if (size == "small"):
        if (style == "regular"):
            price = 12.70
        elif (style == "sicilian"):
            price = 24.45
    elif (size == "large"):
        if (style == "regular"):
            price = 17.95
        elif (style == "sicilian"):
            price = 38.70

    pizza = Pizza(style = style, size = size, price = price)
    
    if (name in orders):
        orders[name][0].append(pizza)
        orderPrice = orders[name][1] 
        orders[name][1] = orderPrice + price
    else:
        orders[name] = [[pizza], price]
    
    print(orders)
    return orderPizza(request)

def viewCart(request, name):
    orderList = orders[name][0]
    orderPrice = orders[name][1]
    context = {
        "orderList": orderList,
        "name": name,
        "total price": orderPrice
    }

    return render(request, "orders/viewCart.html", context)


