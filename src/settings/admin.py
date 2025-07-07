from django.contrib import admin
from settings.models import Settings, TelegramChannel

class TelegramChannelAdmin(admin.ModelAdmin):
    list_display = ("bot_username", "user", "updated_at", "created_at", "is_connect")
admin.site.register(TelegramChannel, TelegramChannelAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ("IR_yearly", "IR_monthly", "TR_yearly", "TR_monthly", "token1M")
admin.site.register(Settings, SettingsAdmin)