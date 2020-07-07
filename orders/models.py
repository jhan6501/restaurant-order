from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length = 64)
    orderPrice = models.FloatField()

    def __str__(self):
        return f"An order for {self.name} that costs a total of {self.orderPrice}"


class Pizza(models.Model):
    style = models.CharField(max_length = 64)
    size = models.CharField(max_length = 64)
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "pizza", blank = True, null = True)

    def __str__(self):
        
        return f"A {self.size} {self.style} pizza that costs {self.price}"


class burgerTopping(models.Model):
    name = models.CharField(max_length = 64, unique = True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} - ${self.price}"


class Burger(models.Model):
    size = models.CharField(max_length = 64)
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "burger", blank = True, null = True)
    toppings = models.ManyToManyField(burgerTopping, blank = True, related_name = "burger")
    
    # def returnToppings(self):
        

    def __str__(self):
        return f"A {self.size} burger that costs {self.price} with topping list of: {self.toppings.all()}"


