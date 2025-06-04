from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']

        # You can now process or store this message, or send it over WebSocket

        # Optional: respond back
        # send_telegram_message(chat_id, "Received your message!")

        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "invalid"})
