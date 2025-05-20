from rest_framework import serializers
from accounts.serializers.user import UserShortSerializer
from accounts.functions import login
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        try:
            access, refresh = login(user)
        except Exception as e:
            raise serializers.ValidationError(f"Token generation error: {str(e)}")
        return {
            "refresh_token": refresh,
            "access_token": access,
            "user_data": UserShortSerializer(user).data,
        }


class CompleteRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','age','gender','address','organisation','description','state','zip_code','country','language','time_zone','currency')