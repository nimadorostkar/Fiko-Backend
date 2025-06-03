from rest_framework.views import APIView
from rest_framework.response import Response
from message.serializers import TagSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from message.models import Tag


class TagsAPIView(APIView):
    serializer_class = TagSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        try:
            tag = Tag.objects.all()
            serializer = self.serializer_class(tag, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)

