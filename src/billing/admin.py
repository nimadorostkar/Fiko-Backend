from django.contrib import admin
from billing.models import Purchases
from import_export.admin import ImportExportModelAdmin

class PurchasesAdmin(ImportExportModelAdmin):
    list_display = ('user', 'price', 'created_at', 'paid')
    list_filter = ("created_at", "user", "paid")
admin.site.register(Purchases, PurchasesAdmin)
