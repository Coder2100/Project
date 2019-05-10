from django.http import HttpResponse
from django.shortcuts import render
# import Order model from model
#from .models import Order

# Create your views here.
def index(request):
   # return HttpResponse("Project 3: TODO")
   return render(request, "orders/index.html")
