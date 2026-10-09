from django.db import models
from django.conf import settings

from core.models import BaseModel
from post.models import Post

class Like(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user','post'), name='unique_like_relation')
        ]

    def __str__(self):
        return f"{self.user.username} likes post {self.post_id}"
