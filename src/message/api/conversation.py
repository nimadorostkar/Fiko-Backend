from rest_framework.views import APIView
from rest_framework.response import Response
from message.serializers import ConversationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from message.models import Conversation


class UserConversationsAPIView(APIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        try:
            plan = Conversation.objects.filter(user=self.request.user)
            serializer = self.serializer_class(plan)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Conversations not found or something went wrong, try again", status=status.HTTP_400_BAD_REQUEST)