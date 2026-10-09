from django.db.models import Count, Exists, OuterRef
from django.shortcuts import get_object_or_404

from .models import Post
from like.models import Like


def get_posts(user):
    user_likes = Like.objects.filter(user=user, post=OuterRef('pk'))

    return (Post.objects.select_related('author').annotate(likes_count=Count('likes'),is_liked=Exists(user_likes)).order_by('-created_at'))


def get_post_by_pk(pk, user):
    user_likes = Like.objects.filter(user=user,post=OuterRef('pk'))

    return get_object_or_404(Post.objects.select_related('author').annotate(likes_count=Count('likes'),is_liked=Exists(user_likes)), pk=pk)