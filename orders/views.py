from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from itertools import chain
from operator import attrgetter

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

def orderBurger(request):
    name = request.POST['user']
    sizes = ["small", "large"]
    toppingList = burgerTopping.objects.all()
    context = {
        "name": name,
        "sizes": sizes, 
        "toppingList": toppingList
    }

    return render(request, "orders/orderBurger.html", context)

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

def addCartBurger(request):
    name = request.POST['user']
    size = request.POST['size']
    price = float(request.POST['price'])
    selectedTopping = request.POST.getlist('topping')

    print (selectedTopping)
    burger = Burger(size = size, price = price)
    burger.save()
    for toppingName in selectedTopping:
        topping = burgerTopping.objects.get(name = toppingName)
        print (topping)
        burger.toppings.add(topping)
        print(burger.toppings)
        
    print(burger)

    print ("test1")

    if (name in orders):
        orders[name][0].append(burger)
        orderPrice = orders[name][1] 
        orders[name][1] = orderPrice + price
    else:
        orders[name] = [[burger], price]
    
    print ("test2")

    print (orders)
    return orderBurger(request)

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
    burgerList = Burger.objects.filter(order = order)
    
    foodList = chain(pizzaList,burgerList)
    
    print ("The price of the order is: " + str(order.orderPrice))
    context = {
        "name": name, 
        "foodList": foodList,
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
    burgerList = Burger.objects.filter(order = order)
    print(order)
    context = {
        "order": order,
        "pizzaList": pizzaList,
        "burgerList": burgerList
    }

    return render(request, "restaurant/viewOrder.html", context)

def deletePizza(request): 
    orderId = request.POST["orderId"]
    pizzaId = request.POST["pizzaId"]
    
    order = Order.objects.get(id = orderId)
    removePizza = Pizza.objects.get(id = pizzaId)

    order.orderPrice = order.orderPrice - removePizza.price
    order.save()
    print (order.orderPrice)
    Pizza.objects.filter(id = pizzaId).delete()
    return viewOrder(request, orderId)

def deleteBurger(request): 
    orderId = request.POST["orderId"]
    burgerId = request.POST["burgerId"]
    
    order = Order.objects.get(id = orderId)
    removeBurger = Burger.objects.get(id = burgerId)

    order.orderPrice = order.orderPrice - removeBurger.price
    order.save()
    print (order.orderPrice)
    Burger.objects.filter(id = burgerId).delete()
    return viewOrder(request, orderId)

def deleteOrder(request):
    orderId = request.POST["orderId"]
    Order.objects.filter(id = orderId).delete()

    return allOrders(request)

def burgerToppingPage(request):
    toppingList = burgerTopping.objects.all()

    context = {
        "toppingList": toppingList
    }

    return render(request, "restaurant/addBurgerTopping.html", context)
    
def addBurgerTopping(request):
    toppingName = request.POST["topping"]
    toppingPrice = float(request.POST["price"])

    topping = burgerTopping(name = toppingName, price = toppingPrice)
    topping.save()

    return burgerToppingPage(request)




