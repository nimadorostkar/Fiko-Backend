from django.shortcuts import render
from settings.serializers import TelegramChannelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from settings.models import Settings,TelegramChannel
import requests
from django.http import JsonResponse


class ConnectTeleAPIView(APIView):
    serializer_class = TelegramChannelSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = request.user.id

        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        channel = serializer.save()
        webhook_url = self._build_webhook_url(data["bot_token"], data["bot_username"])

        try:
            response = requests.post(webhook_url)
            if response.status_code == 200:
                channel.is_connect = True
                channel.save()
            else:
                return Response(
                    {"error": f"Telegram API responded with status {response.status_code}: {response.text}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except requests.exceptions.RequestException as e:
            # Optional: log the error using Django's logging
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer_class(channel).data, status=status.HTTP_201_CREATED)

    def _build_webhook_url(self, bot_token, bot_username):
        """
        Builds the full Telegram API webhook URL for setting the bot's webhook.
        """
        base_url = f"https://api.telegram.org/bot{bot_token}/setWebhook"
        webhook_target = f"https://api.fiko.net/api/v1/message/webhook/{bot_username}/"
        return f"{base_url}?url={webhook_target}"




"""   
class ConnectTeleAPIView(APIView):
    serializer_class = TelegramChannelSerializer
    permission_classes = [IsAuthenticated]
    def post(self, *args, **kwargs):
        data = self.request.data
        data["user"] = self.request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            channel = serializer.save()

            url = f"https://api.telegram.org/bot{data['bot_token']}/setWebhook"
            params = {
                "url": f"https://api.fiko.net/api/v1/message/webhook/{data['bot_username']}/"
            }
            try:
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    channel.is_connect=True
                    channel.save()
            except requests.exceptions.RequestException as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(channel)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
"""