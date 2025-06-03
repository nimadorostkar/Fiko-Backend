from django.urls import path
from message.api import FullUserConversationsAPIView,UserConversationsAPIView,ConversationItemAPIView,TagsAPIView

urlpatterns = [
    path("tags", TagsAPIView.as_view(), name="tags"),
    path("user-conversation", UserConversationsAPIView.as_view(), name="user-conversation"),
    path("user-conversation-full", FullUserConversationsAPIView.as_view(), name="user-conversation-full"),
    path("conversation-item/<str:id>/", ConversationItemAPIView.as_view(), name="conversation-item"),
]