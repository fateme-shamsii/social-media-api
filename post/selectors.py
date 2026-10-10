from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404

from .models import Post
from like.models import Like
from comment.models import Comment


def get_posts(user):
    user_likes = Like.objects.filter(user=user, post=OuterRef('pk'))
    user_comments = Comment.objects.filter(author=user, post=OuterRef('pk'))

    return (Post.objects.select_related('author').annotate(likes_count=Count('likes', distinct=True),comments_count=Count('comments', distinct=True), is_commented=Exists(user_comments) ,is_liked=Exists(user_likes)).order_by('-created_at'))


def get_post_by_pk(pk, user):
    user_likes = Like.objects.filter(user=user, post=OuterRef('pk'))
    user_comments = Comment.objects.filter(author=user, post=OuterRef('pk'))

    return get_object_or_404(Post.objects.select_related('author').annotate(likes_count=Count('likes', distinct=True), comments_count=Count('comments', distinct=True)
                            ,is_liked=Exists(user_likes), is_commented=Exists(user_comments)), pk=pk)

