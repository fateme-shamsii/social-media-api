from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .serializers import CreateUserSerializer

class CreateUserView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'username': user.username,
            'email': user.email,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        },status=status.HTTP_201_CREATED)





