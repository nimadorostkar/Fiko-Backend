from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import refresh as refresh_function
from core.settings import ACCESS_TTL

class RefreshAccess(APIView):
    permission_classes = []

    def post(self, *args, **kwargs):
        refresh = self.request.data.get("refresh", "")

        try:
            access, refresh = refresh_function(refresh)
        except ValueError:
            return Response(
                {"success": False, "errors": [_("refresh is invalid")]},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        response = Response({
            "success": True,
            "data": {"refresh_token": refresh, "access_token": access}
             },
            status=status.HTTP_200_OK,
        )
        response.set_cookie(
            key="HTTP_ACCESS",  # or "jwt" depending on your code
            value=f"Bearer {access}",
            httponly=True,
            max_age=ACCESS_TTL * 24 * 3600,
            secure=False,  # set to False for local development
            samesite='Lax')
        return response