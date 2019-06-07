from django.db import models
from django.conf import settings

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
class Topping(models.Model):
    name=models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class RegularPizza(models.Model):
    pizza= models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="regular_price")
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"
class SicilianPizza(models.Model):
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="sicilian_price")
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"
class Sub(models.Model):
    name=models.CharField(max_length=64)
    small=models.DecimalField(max_digits=4,decimal_places=2)
    large=models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.small} -{self.large}"

class DinnerPlatter(models.Model):
     name=models.CharField(max_length=64)
     small=models.DecimalField(max_digits=4,decimal_places=2)
     large=models.DecimalField(max_digits=4,decimal_places=2)

     def __str__(self):
         return f"{self.name} - {self.small} -{self.large}"

class Pasta(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Salad(models.Model):
    name=models.CharField(max_length=64)
    price=models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"
        









