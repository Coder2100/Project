from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sicilian", views.sicilian, name="sicilian"),
]

