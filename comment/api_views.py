from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .permissions import IsOwnerComment
from .serializers import CreateCommentSerializer,ShowCommentForAllPostSerializer,EditCommentSerializer
from .selectors import get_post,get_comments_for_post,get_comment_by_pk

class CommentForPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_post(pk)

    
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, post=post)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        comments = get_comments_for_post(pk)

        serializer = ShowCommentForAllPostSerializer(comments, many=True)

        return Response(serializer.data)

class CommentDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerComment]

    def patch(self, request, pk):
        comment = get_comment_by_pk(pk)

        self.check_object_permissions(request, comment)

        serializer = EditCommentSerializer(
            comment,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        comment = get_comment_by_pk(pk)

        self.check_object_permissions(request, comment)

        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)