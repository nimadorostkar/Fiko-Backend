from django.urls import path
from settings.views import PricesAPIView
from settings.channels_view import ConnectTeleAPIView,DisConnectTeleAPIView,TeleBotAPIView

urlpatterns = [
    # channels
    path("tele-bot", TeleBotAPIView.as_view(), name="tele-bot"),
    path("connect-tele-bot", ConnectTeleAPIView.as_view(), name="connect-tele-bot"),
    path("dis-tele/<str:bot_name>/", DisConnectTeleAPIView.as_view(), name="dis-tele"),
    # prices
    path("prices", PricesAPIView.as_view(), name="prices"),
]