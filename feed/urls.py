from django.urls import path
from . import api_views

urlpatterns = [
    path('post/', api_views.FeedView.as_view(), name='feed'),
]