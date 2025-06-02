from django.urls import path
from billing.api import CurrentPlanAPIView,Payment,PaymentVerify#,PaymentHistory

urlpatterns = [
    path("current-plan", CurrentPlanAPIView.as_view(), name="current-plan"),
    path("payment", Payment.as_view(), name="payment"),
    path("payment-verify/<int:id>/", PaymentVerify.as_view(), name="payment-verify"),
    #path("payment-history",PaymentHistory.as_view(),name="pay-history"),
]