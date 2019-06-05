from django.contrib import admin

from accounts.views import login_view, register
from .models import Pasta, MenuCatalogue, Topping,Salad,SicilianPizza, RegularPizza,Sub,DinnerPlatter, Pizza
#from accounts.views import Orders


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizza_toppings", "sub_additions")

# Register your models here.
admin.site.register(Pasta)
admin.site.register(MenuCatalogue)
admin.site.register(Topping)
admin.site.register(DinnerPlatter)
admin.site.register(Salad)
admin.site.register(SicilianPizza)
admin.site.register(RegularPizza)
admin.site.register(Sub)
admin.site.register(Pizza)
#admin.site.register(Orders, OrderAdmin)

