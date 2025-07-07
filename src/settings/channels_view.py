from django.shortcuts import render
from settings.serializers import TelegramChannelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from settings.models import Settings,TelegramChannel


class ConnectTeleAPIView(APIView):
    serializer_class = TelegramChannelSerializer
    permission_classes = [IsAuthenticated]
    def post(self, *args, **kwargs):
        data = self.request.data
        data["user"] = self.request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
