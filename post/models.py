from django.db import models
from core.models import BaseModel
from django.conf import settings


class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return f"{self.author.username} - {self.id}"