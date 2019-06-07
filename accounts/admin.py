from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from .models import Profile
from .views import Orders, Confirmations

@admin.register(Confirmations)
class ExportConfirmation(ImportExportModelAdmin):
    list_display = ('title','price', 'order_status', 'username')
    list_filter = ('time',)
    pass
@admin.register(Orders)
class ExportOrders(ImportExportModelAdmin):
    list_display = ('title','price', 'order_status', 'username')
    list_filter = ('time',)
    pass

admin.site.register(Profile)

admin.site.site_header =  "Pinocchio's Pizza & Subs"

