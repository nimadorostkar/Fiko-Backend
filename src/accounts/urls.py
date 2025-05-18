from django.urls import path
from accounts.views import Profile,Refresh,RefreshAccess,OverView,Login

urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("profile", Profile.as_view(), name="profile"),
]