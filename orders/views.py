from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
# import Order model from model


# Create your views here.
def index(request):
   # return HttpResponse("Project 3: TODO")
   return render(request, "orders/index.html")
def sicilian(request):
    return render(request, "orders/sicilian.html")







