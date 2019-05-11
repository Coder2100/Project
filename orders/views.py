from django.http import HttpResponse
from django.shortcuts import render
# import Order model from model
#from .models import Order

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
    return render(request, "orders/menu.html")

