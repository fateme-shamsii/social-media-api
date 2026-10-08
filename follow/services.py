from rest_framework.exceptions import ValidationError

from .models import Follow


def follow_user(follower, following):
    if follower == following:
        raise ValidationError("You can't follow yourself.")

    if Follow.objects.filter(follower=follower, following=following).exists():
        raise ValidationError("You already follow this user.")

    return Follow.objects.create(
        follower=follower,
        following=following
    )