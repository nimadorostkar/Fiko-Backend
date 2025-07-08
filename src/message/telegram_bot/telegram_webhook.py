from django.http import JsonResponse
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from message.models import Customer,Conversation,Message
from settings.models import TelegramChannel


class TelegramWebhook(APIView):
    permission_classes = [AllowAny]
    def post(self, *args, **kwargs):
        try:
            data = json.loads(self.request.body.decode("utf-8"))
            user_info = data['message']['from']
            chat_id = data['message']['chat']['id']
            message_text = data['message']['text']
            telegram_id = user_info['id']
            first_name = user_info.get('first_name', '')
            last_name = user_info.get('last_name', '')
            bot_name = self.kwargs["bot_name"]

            channel = TelegramChannel.objects.get(bot_username=bot_name)
            bot_user = channel.user

            # Create or update Customer
            customer, created = Customer.objects.update_or_create(
                source='telegram',source_id=telegram_id,
                defaults={'first_name':first_name,'last_name':last_name,}
            )
            action = "created" if created else "updated"
            print(f"Customer {action}: {customer}")

            # Create or update Conversation
            conversation, created = Conversation.objects.update_or_create(
                user=bot_user,source='telegram', customer=customer,
            )
            action = "created" if created else "updated"
            print(f"Conversation {action}: {conversation}")

            # Create Message
            message = Message.objects.create(content=message_text, conversation=conversation, customer=customer,)
            print(f"Message created: {message}")

            # You can now process or store this message, or send it over WebSocket
            # Optional: respond back
            # send_telegram_message(chat_id, "Received your message!")

            return JsonResponse({"status": "ok"})
        except Exception as e:
            return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)
