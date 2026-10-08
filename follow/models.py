from django.db import models
from core.models import BaseModel
from django.conf import settings

class Follow(BaseModel):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_relations')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower_relations')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('follower', 'following'), name='unique_follow_relation'),
            models.CheckConstraint(condition=~models.Q(follower=models.F('following')), name='prevent_self_follow')
        ]

    def __str__(self):
        return f"{self.follower} follows {self.following}"

