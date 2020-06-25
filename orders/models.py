from django.db import models

# Create your models here.
class Food(models.Model):
    class Meta: 
        abstract = True

class Pizza(Food):
    style = models.CharField(max_length = 64)
    size = models.CharField(max_length = 64)
    price = models.FloatField()

    def __str__(self):
        return f"A {self.size} {self.type} pizza that is {self.toppings} that costs {self.price}"
