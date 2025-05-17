from django.contrib import admin
from django.urls import path, include
from core import views as HomeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeViews.index, name='home'),
    path("api/v1/accounts/", include("apps.accounts.urls")),
]
