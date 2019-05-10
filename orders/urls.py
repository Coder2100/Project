from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
   # path("/sicilian_regualar", sicilian_regualar, name="sicilian_regualar")
]
