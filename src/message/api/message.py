from rest_framework.response import Response
from message.serializers import MessageSerializer
from rest_framework import status, filters
from message.models import Message
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500


class UserMessagesAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content',]
    ordering_fields = ['created_at',]
    filterset_fields = ['created_at','is_answered','is_ai_response','conversation','type']
    @swagger_auto_schema()
    def get(self, request, format=None):
        query = self.filter_queryset(Message.objects.filter(conversation__user=self.request.user))
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
