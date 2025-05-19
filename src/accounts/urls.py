from django.urls import path
from accounts.api import LoginAPIView,RegisterView,CompleteRegisterView

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='register'),
    path('complete', CompleteRegisterView.as_view(), name='complete'),
]