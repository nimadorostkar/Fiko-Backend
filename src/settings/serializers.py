from rest_framework import serializers
from settings.models import Settings,TelegramChannel

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        #fields = '__all__'
        exclude = ['id']


class TelegramChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramChannel
        fields = '__all__'