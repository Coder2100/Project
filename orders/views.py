from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse
# import Order model from model
from .models import Pasta, MenuCatalogue, Topping, RegularPizza, SicilianPizza, SicilianPizza, Sub,Salad # DinnerPlatter

# Create your views here.
def index(request):
   # return HttpResponse("Project 3: TODO")

   return render(request, "orders/index.html")

def sicilian(request):
    return render(request, "orders/sicilian.html")

def register(request):
    return render(request, "orders/register.html")

def login(request):
    return render(request, "orders/login.html")
def logout(request):
    return render(request, "orders/logout.html")

def menu(request):

   context = {
      "pastas": Pasta.objects.all(),
      "menuCatalogues": MenuCatalogue.objects.all(),
      "toppings": Topping.objects.all(),
      "regularyPizzas": RegularPizza.objects.all(),
      "sicilianPizzas": SicilianPizza.objects.all(),
      "subs": Sub.objects.all(),
     # "dinnerPlatters": DinnerPlatter.objects.all(),
      "salads": Salad.objects.all()

   }
   return render(request, "orders/menu.html", context)


