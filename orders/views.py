from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    return render(request, "orders/menu.html")

def orderPizza(request):
    name = ""
    foodItem = "Pizza"
    sizes = ["small", "medium", "large"]
    types = ["regular", "sicilian"]
    context = {
        "food": foodItem,
        "sizes": sizes,
        "types": types,
    }

    return render(request, "orders/orderPizza.html", context)


