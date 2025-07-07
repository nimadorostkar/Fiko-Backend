from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import traceback
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated


class TelegramWebhook(APIView):
    permission_classes = [AllowAny]
    def post(self, bot_name=None, *args, **kwargs):
        try:
            data = json.loads(self.request.body.decode("utf-8"))
            user_info = data['message']['from']

            print(("---"))
            chat_id = data['message']['chat']['id']
            message_text = data['message']['text']
            telegram_id = user_info['id']
            first_name = user_info.get('first_name', '')
            last_name = user_info.get('last_name', '')
            print(chat_id)
            print(message_text)
            print(telegram_id)
            print(first_name)
            print(bot_name)


            # You can now process or store this message, or send it over WebSocket
            # Optional: respond back
            # send_telegram_message(chat_id, "Received your message!")
            return JsonResponse({"status": "ok"})
        except Exception as e:
            return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']

        print(chat_id)
        print(message_text)
        print("---------")
        print(data)

        # You can now process or store this message, or send it over WebSocket
        # Optional: respond back
        # send_telegram_message(chat_id, "Received your message!")

        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "invalid"})
