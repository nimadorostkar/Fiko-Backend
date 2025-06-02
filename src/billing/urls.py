from django.urls import path
from billing.api import CurrentPlanAPIView

urlpatterns = [
    path("current-plan", CurrentPlanAPIView.as_view(), name="current-plan"),
]