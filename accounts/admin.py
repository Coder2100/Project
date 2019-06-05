from django.contrib import admin
from .models import Profile
from .views import Orders, Confirmations
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ("pizza_toppings", "sub_additions")

admin.site.register(Profile)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Confirmations)
