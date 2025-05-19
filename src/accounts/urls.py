from django.urls import path
from accounts.api import LoginAPIView,RegisterView

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='register'),
    #path("profile", Profile.as_view(), name="profile"),
]