from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

orders = {}

def index(request):
    context = {
        "firstLoad": True
    }
    return render(request, "orders/menu.html", context)

def menu(request, name):
    context = {
        "firstLoad": False,
        "name": name
    }
    print ("test for menu")
    return render(request, "orders/menu.html", context)

def orderPizza(request):
    name = request.POST['user']
    print ("test for order pizza")
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

# def viewCart (request):
#     print("test")
#     return orderPizza(request)

def viewCart(request, name):
    orderList = orders[name][0]
    orderPrice = orders[name][1]
    context = {
        "orderList": orderList,
        "name": name,
        "totalPrice": orderPrice
    }
    return render(request, "orders/viewCart.html", context)

def placeOrder(request, name):
    orderList = orders[name][0]
    orderPrice = orders[name][1]
    if (Order.objects.filter(name = name).count() == 0):
        order = Order(name = name, orderPrice = orderPrice)
        order.save()

        for food in orderList:
            food.order = order
            food.save()
    
    else:
        order = Order.objects.get(name = name) 

        for food in orderList:
            food.order = order
            food.save()
            
        print(order)
        print ("the price of order before update is:" + str(order.orderPrice))
        order.orderPrice = order.orderPrice + orderPrice
        print ("the price of order afters update is:" + str(order.orderPrice))
        order.save()
    
    return index(request)

def trackOrder(request):
    print ("test 1") 
    name = request.POST['user']

    print ("test 2") 
    order = Order.objects.get(name = name)

    print ("test 3")
    pizzaList = Pizza.objects.filter(order = order)

    print(pizzaList)
    print ("The price of the order is: " + str(order.orderPrice))
    context = {
        "name": name, 
        "pizzaList": pizzaList,
        "totalPrice": order.orderPrice
    }

    return render(request, "orders/trackOrder.html", context)

def allOrders(request):

    orderList = Order.objects.all()

    context = {
        "orderList": orderList
    }

    return render(request, "restaurant/allOrders.html", context)

def viewOrder(request, order_id):
    order = Order.objects.get(pk = order_id)
    pizzaList = Pizza.objects.filter(order = order)
    
    print(order)    
    print(pizzaList)

    context = {
        "order": order,
        "pizzaList": pizzaList
    }

    return render(request, "restaurant/viewOrder.html", context)

def deletePizza(request): 
    orderId = request.POST["orderId"]
    pizzaId = request.POST["pizzaId"]
    
    order = Order.objects.filter(id = orderId)
    removePizza = Pizza.objects.filter(id = pizzaId)

    order.orderPrice = order.orderPrice - removePizza.price
    Pizza.objects.filter(id = pizzaId).delete()
    return viewOrder(request, orderId)

def deleteOrder(request):
    orderId = request.POST["orderId"]
    Order.objects.filter(id = orderId).delete()

    return allOrders(request)



