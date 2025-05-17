from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import NotificationSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.models import Notification


class Notifications(APIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        try:
            notifs = Notification.objects.filter(user=self.request.user,seen=False)
            serializer = self.serializer_class(notifs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)


    def patch(self, *args, **kwargs):
        try:
            notif_ids = self.request.data.get('notifications', [])
            notifications = Notification.objects.filter(user=self.request.user, id__in=notif_ids)
            notifications.update(seen=True)
            return Response("Notifications have been seen.", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)