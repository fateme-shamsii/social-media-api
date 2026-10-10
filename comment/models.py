from django.db import models
from django.conf import settings

from core.models import BaseModel
from post.models import Post


class Comment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return f'{self.author.username} commented on post {self.post_id}'