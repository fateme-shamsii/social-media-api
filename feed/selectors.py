from follow.models import Follow
from post.models import Post

def get_feed_posts(user, search=None):
    following_ids = Follow.objects.filter(
        follower=user
    ).values_list('following_id', flat=True)

    posts = Post.objects.filter(author__in=following_ids)

    if search:
        posts = posts.filter(caption__icontains=search)

    return posts.order_by('-created_at')

