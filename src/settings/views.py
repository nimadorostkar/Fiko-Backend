from django.shortcuts import render
from settings.serializers import SettingsSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from settings.models import Settings

class PricesAPIView(APIView):
    serializer_class = SettingsSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        try:
            prices = Settings.objects.get(id=1)
            serializer = self.serializer_class(prices)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Prices not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)
