from django.contrib import admin
from accounts.models import User
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = "Fiko Admin Panel"
admin.site.site_title = "Fiko"
admin.site.index_title = "Fiko Dashboard"

class UserAdmin(ImportExportModelAdmin):
    field_list = (
    'is_profile_fill','id','first_name','last_name','email','phone_number','username','age','gender','organisation',
    'address', 'description','profile_picture','password','last_login','is_superuser','state','zip_code','country',
    'is_staff','is_active','date_joined','updated_at','created_at','language','time_zone','currency')

    list_display = ('img_tag','email','username','id','first_name','last_name','is_profile_fill','created_at')
    list_filter = ("country","gender","created_at","updated_at")
    search_fields = ['email','username','phone_number','first_name','last_name']
    readonly_fields = field_list
    fields = field_list
admin.site.register(User, UserAdmin)
