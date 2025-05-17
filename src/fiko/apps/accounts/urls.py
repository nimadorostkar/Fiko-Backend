from django.urls import path
from fiko.apps.accounts.views import Logout,Profile,Refresh,RefreshAccess,OverView,SendOTP,VerifyOTP,ProfilePicture,Notifications

urlpatterns = [
    #path("otp", SendOTP.as_view(), name="send_otp"),
    #path("otp/verify", VerifyOTP.as_view(), name="verify_otp"),
    #path("refresh", Refresh.as_view(), name="refresh"),
    #path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    #path("logout", Logout.as_view(), name="logout"),
    #path("profile", Profile.as_view(), name="profile"),
    #path("profile/picture", ProfilePicture.as_view(), name="profile-picture"),
    #path("notifications", Notifications.as_view(), name="notifications"),
    path("overview", OverView.as_view(), name="overview"),
]