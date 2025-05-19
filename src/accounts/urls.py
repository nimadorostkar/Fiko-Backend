from django.urls import path
from accounts.api import LoginAPIView,RegisterView,CompleteRegisterView,Refresh,RefreshAccess,Logout,Profile,ProfilePicture

urlpatterns = [
    path("login", LoginAPIView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='register'),
    path('complete', CompleteRegisterView.as_view(), name='complete'),
    path("refresh", Refresh.as_view(), name="refresh"),
    path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    path("logout", Logout.as_view(), name="logout"),
    path("profile", Profile.as_view(), name="profile"),
    path("profile-pic", ProfilePicture.as_view(), name="profile-pic"),
]