
from django.shortcuts import render, redirect
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
#from orders.models import Order



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
