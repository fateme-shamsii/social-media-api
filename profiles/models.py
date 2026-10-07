from django.conf import settings
from django.db import models
from core.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11, blank=True)
    date_birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
