from rest_framework.views import APIView
from rest_framework.response import Response
from message.serializers import ConversationSerializer
from rest_framework import status, filters
from message.models import Conversation
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500

class FullUserConversationsAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = ConversationSerializer
    #queryset = Conversation.objects.filter(user=self.request.user)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title',]
    ordering_fields = ['created_at','updated_at','priority']
    filterset_fields = ['created_at','updated_at','priority','status','is_active','source']
    @swagger_auto_schema()
    def get(self, request, format=None):
        query = self.filter_queryset(Conversation.objects.filter(user=self.request.user))
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UserConversationsAPIView(APIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        try:
            conv = Conversation.objects.filter(user=self.request.user)
            serializer = self.serializer_class(conv, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)



class ConversationItemAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConversationSerializer
    def get(self, *args, **kwargs):
        try:
            conv = Conversation.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(conv)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)