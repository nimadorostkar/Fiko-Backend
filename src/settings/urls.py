from django.urls import path
from settings.views import PricesAPIView
from settings.channels_view import ConnectTeleAPIView


urlpatterns = [
    # channels
    path("connect-tele-bot", ConnectTeleAPIView.as_view(), name="connect-tele-bot"),
    # prices
    path("prices", PricesAPIView.as_view(), name="prices"),
]


