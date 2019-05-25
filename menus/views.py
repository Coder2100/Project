from django.shortcuts import render
from django.urls import reverse

from .models import Pasta, MenuCatalogue, Topping, RegularPizza, SicilianPizza, SicilianPizza, Sub,Salad, DinnerPlatter
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts:login')
def menu(request):
   context = {
      "pastas": Pasta.objects.all(),
      "menuCatalogues": MenuCatalogue.objects.all(),
      "toppings": Topping.objects.all(),
      "regularyPizzas": RegularPizza.objects.all(),
      "sicilianPizzas": SicilianPizza.objects.all(),
      "subs": Sub.objects.all(),
      "dinnerPlatters": DinnerPlatter.objects.all(),
      "salads": Salad.objects.all()

   }
   return render(request, "menus/menu.html", context)