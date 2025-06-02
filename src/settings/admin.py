from django.contrib import admin
from settings.models import Settings
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("IR_yearly", "IR_monthly", "TR_yearly", "TR_monthly", "token1M")
admin.site.register(Settings, SettingsAdmin)