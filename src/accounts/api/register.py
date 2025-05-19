from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import RegisterSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from core.settings import ACCESS_TTL

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.create(serializer.validated_data)
            response = Response(result, status=status.HTTP_201_CREATED)
            response.set_cookie("HTTP_ACCESS", f"Bearer {result['access_token']}",
                                max_age=ACCESS_TTL * 24 * 3600,
                                secure=True, httponly=True, samesite="None",)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompleteRegisterView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def patch(self, *args, **kwargs):
        serializer = self.serializer_class(self.request.user, data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)