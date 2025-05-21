from django.contrib import admin
from django.urls import path,include
from core import views
from django.conf.urls.static import static
from core.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Fiko APIs",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@fiko.net"),
        license=openapi.License(name="Fiko License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path("api/v1/usr/", include("accounts.urls")),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)