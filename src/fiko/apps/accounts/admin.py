from django.contrib import admin
from fiko.apps.accounts.models import User,Notification
from import_export.admin import ImportExportModelAdmin

class UserAdmin(ImportExportModelAdmin):
    list_display = ('phone_number', 'id', 'first_name', 'last_name', 'created_at')
    list_filter = ("created_at","invite_code")
    search_fields = ['phone_number', 'first_name', 'last_name']
    readonly_fields = ('phone_number','invite_code','updated_at','created_at')
    fields = ('phone_number', 'invite_code', 'first_name', 'last_name', 'image', 'birth_date', 'updated_at', 'created_at')
admin.site.register(User, UserAdmin)


class NotificationAdmin(ImportExportModelAdmin):
    list_display = ('user', 'created_at', 'seen')
    list_filter = ("created_at","seen")
    search_fields = ['notification',]
admin.site.register(Notification, NotificationAdmin)