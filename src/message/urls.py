from django.urls import path
from message.api import UserConversationsAPIView

urlpatterns = [
    path("user-conversation", UserConversationsAPIView.as_view(), name="user-conversation"),
]