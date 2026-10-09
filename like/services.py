from .models import Like
from rest_framework.exceptions import ValidationError

def like_post(user, post):
    if Like.objects.filter(user=user, post=post).exists():
        raise ValidationError("You have already liked this postt")

    return Like.objects.create(user=user, post=post)


def unlike_post(user, post):
    like = Like.objects.filter(user=user, post=post).first()

    if not like:
        raise ValidationError("You have not liked this post.")

    like.delete()