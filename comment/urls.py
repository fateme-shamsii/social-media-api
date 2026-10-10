from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.CommentForPostView.as_view(), name='add-comment'),
    path('<int:pk>/', api_views.CommentDetailView.as_view(), name='comment-detail'), 
]