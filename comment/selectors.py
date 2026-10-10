from django.shortcuts import get_object_or_404

from post.models import Post
from .models import Comment


def get_post(pk):
    return get_object_or_404(Post, pk=pk)

def get_comments_for_post(pk):
    return Comment.objects.select_related('author').filter(post=pk).order_by('-created_at')

def get_comment_by_pk(pk):
    return get_object_or_404(
        Comment.objects.select_related('author', 'post'),
        pk=pk
    )

