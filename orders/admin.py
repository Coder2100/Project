from django.contrib import admin

#inform admin about my models
from .models import Pasta, MenuCatalogue, Topping,Salad,SicilianPizza, RegularPizza,Sub,DinnerPlatter

# Register your models here.
admin.site.register(Pasta)
admin.site.register(MenuCatalogue)
admin.site.register(Topping)
admin.site.register(DinnerPlatter)
admin.site.register(Salad)
admin.site.register(SicilianPizza)
admin.site.register(RegularPizza)
admin.site.register(Sub)
