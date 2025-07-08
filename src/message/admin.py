from django.contrib import admin
from message.models import Conversation,Tag,Customer,Message


class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at', 'status')
    list_filter = ("created_at", "status")
admin.site.register(Conversation, ConversationAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
admin.site.register(Tag, TagAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'source',  'created_at', 'id')
    list_filter = ("source", "created_at")
admin.site.register(Customer, CustomerAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'type', 'conversation', 'is_ai_response', 'is_answered',  'created_at', 'id')
    list_filter = ("type", "conversation", "created_at")
admin.site.register(Message, MessageAdmin)