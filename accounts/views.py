
from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth import authenticate
from .forms import MyUserLoginForm, MyUserRegistrationForm
from . models import Profile
from orders.models import Order
from menus.models import Topping, Additions
import stripe 
from datetime import datetime




# Create your views here.

def login_view(request):
    next = request.GET.get('next')
    form = MyUserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('orders:index')
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        form = MyUserRegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email1')
            user.set_password(password)
            user.email = email
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            if next:
                return redirect(next)
            return redirect('orders:index')
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return redirect('orders:index')


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('orders:index')

def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
      'my_orders': my_orders
      }
    return render(request, "accounts/profile.html", context)
class Orders(models.Model):
    dish = models.CharField(max_length=40)
    pizza_type = models.CharField(max_length=40, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
    pizza_toppings = models.ManyToManyField(Topping, related_name="orders", blank=True)
    sub_additions = models.ManyToManyField(Additions, related_name="orders", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=10, default='Draft')

    def to_tuple(self, query, object):
        list = query
        output = []
        if object == 'topping':
            for elem in list:
                output.append(elem.topping)
        else:
            for elem in list:
                output.append(elem.addition)
        return tuple(output)

    def __str__(self):
        return f"{self.id} | {self.dish} Type: {self.pizza_type} Size: {self.size} Toppings: {self.to_tuple(self.pizza_toppings.all(), 'topping')}\
        Additions: {self.to_tuple(self.sub_additions.all(), 'addition')} Price: {self.price} For: {self.username} At: {self.time.hour}:{self.time.minute}-{self.time.day}/{self.time.month}/{self.time.year} Status: {self.order_status}"

class Confirmations(models.Model):
    dish = models.CharField(max_length=40)
    pizza_type = models.CharField(max_length=40, null=True, blank=True)
    size = models.CharField(max_length=15, null=True, blank=True)
    pizza_toppings = models.ManyToManyField(Topping, related_name="confirmations", blank=True)
    sub_additions = models.ManyToManyField(Additions, related_name="confirmations", blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    username = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=10, default='Draft')

    def to_tuple(self, query, object):
        list = query
        output = []
        if object == 'topping':
            for elem in list:
                output.append(elem.topping)
        else:
            for elem in list:
                output.append(elem.addition)
        return tuple(output)

    def __str__(self):
        return f"{self.id} | {self.dish} Type: {self.pizza_type} Size: {self.size} Toppings: {self.to_tuple(self.pizza_toppings.all(), 'topping')}\
        Additions: {self.to_tuple(self.sub_additions.all(), 'addition')} Price: {self.price} For: {self.username} At: {self.time.hour}:{self.time.minute}-{self.time.day}/{self.time.month}/{self.time.year} Status: {self.order_status}"

def added(request):

    dish = request.POST["dish"]
    type = request.POST["type"]
    size = request.POST["size"]
    price = request.POST["price"]

    try:
        topping1 = request.POST["toppings0"]
    except KeyError:
        topping1 = None
    try:
        topping2 = request.POST["toppings1"]
    except KeyError:
        topping2 = None
    try:
        topping3 = request.POST["toppings2"]
    except KeyError:
        topping3 = None
    try:
        topping4 = request.POST["toppings3"]
    except KeyError:
        topping4 = None
    try:
        topping5 = request.POST["toppings4"]
    except KeyError:
        topping5 = None


    if topping1: topping_to_add1 = Toppings.objects.get(id=topping1)
    if topping2: topping_to_add2 = Toppings.objects.get(id=topping2)
    if topping3: topping_to_add3 = Toppings.objects.get(id=topping3)
    if topping4: topping_to_add4 = Toppings.objects.get(id=topping4)
    if topping5: topping_to_add5 = Toppings.objects.get(id=topping5)

   




    order = Orders(dish=dish, pizza_type=type, size=size, price=price, username=request.user.username, order_status="draft")

    order.save()

    if topping1: order.pizza_toppings.add(topping_to_add1)
    if topping2: order.pizza_toppings.add(topping_to_add2)
    if topping3: order.pizza_toppings.add(topping_to_add3)
    if topping4: order.pizza_toppings.add(topping_to_add4)
    if topping5: order.pizza_toppings.add(topping_to_add5)
   

    order.save()

    request.session["blue_cart"] = True

    return JsonResponse({"success": True})

def cart(request):

    orders = Orders.objects.filter(username=request.user.username)

    return render(request, "orders/cart.html", {"orders": orders})

def delete(request):
    id = request.POST["id"]

    try:
        no_content = request.POST["no_content"]
    except KeyError:
        no_content = None

    order = Orders.objects.get(id=id)

    order.delete()

    if no_content == 'no_content':
        request.session["blue_cart"] = False

    return JsonResponse({"success": True})

def checkout(request):


    stripe.api_key = "sk_test_yEFWvn0Ao2NUjFenAxUVcBOA"

    if request.method == 'POST':
        token = request.POST['stripeToken']
        amount = request.POST['amount']

        username = request.POST['username']
        date = datetime.now()



    try:
        charge = stripe.Charge.create(
            amount      = amount,
            currency    = "usd",
            source      = token,
            description = f"Customer: {username}, on {date.day}/{date.month}/{date.year} at {date.hour}:{date.minute}"
        )

    except stripe.error.CardError as ce:
        return False, ce

    else:
        orders = Orders.objects.filter(username=request.user.username)

        for order in orders:
            confirmation = Confirmations(dish=order.dish, pizza_type=order.pizza_type, size=order.size, price=order.price,
            username=order.username, order_status='Confirmed')
            confirmation.save()
            confirmation.pizza_toppings.set(order.pizza_toppings.all())
            confirmation.save()
            order.delete()

        confirmations = Confirmations.objects.filter(username=request.user.username, order_status='Confirmed')
        return render(request, "orders/confirmation.html" , {"confirmations": confirmations} )

