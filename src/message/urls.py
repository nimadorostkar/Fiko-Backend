from django.urls import path
from message.api import FullUserConversationsAPIView,UserConversationsAPIView,ConversationItemAPIView,TagsAPIView,\
    CustomersListAPIView,CustomerItemAPIView,UserMessagesAPIView
from message.telegram_bot import telegram_webhook

urlpatterns = [
    path("tags", TagsAPIView.as_view(), name="tags"),
    path("user-conversation", UserConversationsAPIView.as_view(), name="user-conversation"),
    path("user-conversation-full", FullUserConversationsAPIView.as_view(), name="user-conversation-full"),
    path("conversation-item/<str:id>/", ConversationItemAPIView.as_view(), name="conversation-item"),
    path("customers", CustomersListAPIView.as_view(), name="customers"),
    path("customer-item/<int:id>/", CustomerItemAPIView.as_view(), name="customer-item"),
    path("user-messages", UserMessagesAPIView.as_view(), name="user-messages"),
    path('webhook/', telegram_webhook.as_view(), name='webhook')
]