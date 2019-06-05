from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("checkout", views.checkout, name="checkout"),
    path("cart", views.cart, name="cart"),
    path("delete", views.delete, name="delete"),
    path("added", views.added, name="added"),
]

