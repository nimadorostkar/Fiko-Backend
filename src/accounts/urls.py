from django.urls import path
from accounts.api import LoginAPIView

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    #path("profile", Profile.as_view(), name="profile"),
]