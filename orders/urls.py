from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sicilian", views.sicilian, name="sicilian"),
    path("register", views.register, name="register"),
   # path("login", views.login, name="login"),
    path("login", views.login, name="login"),
    path("logout", views.register, name="logout"),
    path("menu", views.menu, name="menu")
]

