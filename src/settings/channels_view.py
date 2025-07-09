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





class DisConnectTeleAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        bot_name = self.kwargs["bot_name"]
        if not bot_name:
            return Response({"detail": "Bot name is required."},status=status.HTTP_400_BAD_REQUEST)

        try:
            bot = TelegramChannel.objects.get(bot_username=bot_name)
        except TelegramChannel.DoesNotExist:
            return Response({"detail": "Bot not found."}, status=status.HTTP_404_NOT_FOUND)

        if bot.user != self.request.user:
            return Response({"detail": "You do not have permission to remove this bot."},status=status.HTTP_403_FORBIDDEN)

        bot.delete()
        return Response({"detail": "Bot removed successfully."},status=status.HTTP_200_OK)