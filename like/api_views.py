from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from post.models import Post
from .services import like_post,unlike_post

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        like_post(user=request.user, post=post)

        return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        unlike_post(request.user, post)

        return Response(status=status.HTTP_204_NO_CONTENT)




