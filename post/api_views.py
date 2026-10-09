from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import CreatePostSerializer,ShowListPostsSerializer
from .permissions import IsAuthorOrReadOnly
from .selectors import get_posts,get_post_by_pk

class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = get_posts(user=request.user)

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
        post = get_post_by_pk(pk=pk, user=request.user)

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
        
        return Response(status=status.HTTP_204_NO_CONTENT)
