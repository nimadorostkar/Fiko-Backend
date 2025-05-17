from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from fiko.apps.accounts.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from fiko.apps.accounts.models import Notification


class OverView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user=self.request.user
        wallet = Wallet.objects.get(user=user)
        notifs = Notification.objects.filter(user=user,seen=False).order_by('-created_at')
        services = Service.objects.filter(user=user).order_by('-created_at')[:5]
        if wallet.balance < 10000:
            credit = False
        else:
            credit = True

        data = {
            "is_profile_fill": user.is_profile_fill(),
            "user": self.serializer_class(user).data,
            "credit": credit,
            "balance": wallet.balance,
            "notification": notifs.exists(),
            "history": ServiceSerializer(services,many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)