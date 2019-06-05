from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from accounts.views import login_view, register
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










