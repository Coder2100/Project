from django.shortcuts import render
from django.urls import reverse

from .models import Pasta, MenuCatalogue, Topping, RegularPizza, SicilianPizza, SicilianPizza, Sub,Salad, DinnerPlatter
from django.contrib.auth.decorators import login_required
from orders.models import Order

# Create your views here.
@login_required(login_url='accounts:login')
def menu(request):
   filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
   current_order_products = []
   if filtered_orders.exists():
      user_order=filtered_orders[0]
      user_order_items = user_order.items.all()
      current_order_products = [RegularPizza.regular for RegularPizza in user_order_items]
   
   context = {
      "pastas": Pasta.objects.all(),
      "menuCatalogues": MenuCatalogue.objects.all(),
      "toppings": Topping.objects.all(),
      "regularyPizzas": RegularPizza.objects.all(),
      "sicilianPizzas": SicilianPizza.objects.all(),
      "subs": Sub.objects.all(),
      "dinnerPlatters": DinnerPlatter.objects.all(),
      "salads": Salad.objects.all(),
      "current_order_products": current_order_products
   }
   return render(request, "menus/menu.html", context)

   # revisit product model IMPORTANT