from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.functions import login
from django.utils.text import slugify

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        try:
            access, refresh = login(user)
        except Exception as e:
            raise serializers.ValidationError(f"Token generation error: {str(e)}")

        return {
            "refresh_token": refresh,
            "access_token": access,
            "user_data": UserSerializer(user).data,
        }