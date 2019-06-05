from django.urls import path
from django.conf.urls import url
from orders.views import index, sicilian
from . views import (
    index,
    sicilian
)
app_name = 'orders'
urlpatterns = [
    path("",index, name="index"),
    url(r'^sicilian/$',sicilian , name='sicilian'),
]

