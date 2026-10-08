from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .services import follow_user
from .models import Follow
from .serializers import ShowFollowSerializer


class AddFollowView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        User = get_user_model()

        following = get_object_or_404(User, username=username)

        follow_user(request.user, following)
        
        return Response( {"detail": "Followed successfully."},status=status.HTTP_201_CREATED)


class ShowListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        follows = Follow.objects.filter(follower=request.user)
        serializer = ShowFollowSerializer(follows, many=True)

        return Response(serializer.data)




