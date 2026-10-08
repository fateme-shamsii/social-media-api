from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.PostView.as_view(), name='post-list-create'),
    path('<int:pk>/', api_views.PostDetailView.as_view(), name='post-detail'),
]