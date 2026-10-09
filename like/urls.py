from django.urls import path
from . import api_views

urlpatterns = [
    path('<int:post_id>/', api_views.LikePostView.as_view(), name='like_post'),
]