from django.urls import path
from django.conf.urls import url
from orders.views import index, sicilian
from . views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    index,
    sicilian
)
app_name = 'orders'
urlpatterns = [
    path("",index, name="index"),
    url(r'^sicilian/$',sicilian , name='sicilian'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
]

