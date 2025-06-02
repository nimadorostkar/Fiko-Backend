from django.urls import path
from settings.views import PricesAPIView

urlpatterns = [
    path("prices", PricesAPIView.as_view(), name="prices"),
]