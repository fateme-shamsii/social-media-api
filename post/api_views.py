from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from .serializers import CreatePostSerializer,ShowListPostsSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly

class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.select_related('author').order_by('-created_at')
        serializer = ShowListPostsSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class PostDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        print("request user id:", request.user.id)
        print("post author id:", post.author_id)

        self.check_object_permissions(request, post)
        return post

    def get(self, request, pk):
        post = self.get_post(request, pk)

        serializer = ShowListPostsSerializer(post)
        return Response(serializer.data)

    def patch(self, request, pk):
        post = self.get_post(request, pk)

        serializer = CreatePostSerializer(
            post,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        post = self.get_post(request, pk)

        post.delete()
        
        return Response({"detail": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
