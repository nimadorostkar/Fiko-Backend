from rest_framework.views import APIView
from rest_framework.response import Response
from message.serializers import ConversationSerializer,CustomerSerializer
from rest_framework import status, filters
from message.models import Conversation,Customer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500


class CustomersListAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','phone_number','description']
    ordering_fields = ['created_at','updated_at']
    filterset_fields = ['created_at','updated_at','source']
    @swagger_auto_schema()
    def get(self, request, format=None):
        query = self.filter_queryset(Customer.objects.filter(conversations__user=self.request.user).distinct())
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class CustomerItemAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    def get(self, *args, **kwargs):
        try:
            customer = Customer.objects.get(id=self.kwargs["id"])
            serializer = self.serializer_class(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error: {str(e)}", status=status.HTTP_400_BAD_REQUEST)