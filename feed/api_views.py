from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .selectors import get_feed_posts
from post.serializers import ShowListPostsSerializer
from post.pagination import FeedPagination

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        search = request.query_params.get('search')
        posts = get_feed_posts(request.user,search)
        feedpagination = FeedPagination()
        page = feedpagination.paginate_queryset(posts, request, view=self)

        serializer = ShowListPostsSerializer(page, many=True)

        return feedpagination.get_paginated_response(serializer.data)
