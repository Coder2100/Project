from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from accounts.views import login_view, register
from orders.helper import generate_order_id
from menus.models import RegularPizza
from accounts.models import Profile
from orders.models import OrderItem, Order
import datetime

# Create your views here.
def index(request):
   # return HttpResponse("Project 3: TODO")
  
   context = {
       "user":request.user

   }
   return render(request, "orders/index.html", context)
   
def sicilian(request):
    return render(request, "orders/sicilian.html")


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    regular = RegularPizza.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if regular in request.user.profile.pizzas.all():
        messages.info(request, 'You already own this PIZZA')
        return redirect(reverse('menus:menu'))
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(regular=regular)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('menus:menu'))

def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
         item_to_delete[0].delete()
         messages.info(request, "Item has been deleted")
    return redirect(reverse('orders:order_summary'))

def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'orders/order_summary.html', context)








