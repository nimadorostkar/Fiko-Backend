from django.urls import path
from accounts.api import LoginAPIView

urlpatterns = [
    path("aaaa", LoginAPIView.as_view(), name="aaaa"),
]