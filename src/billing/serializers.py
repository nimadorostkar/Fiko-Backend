from rest_framework import serializers
from accounts.models import Plan
from billing.models import Purchases

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = "__all__"