from django.urls import path
from . import api_views

urlpatterns = [
    path('<str:username>/', api_views.AddFollowView.as_view(), name='add-follow'),
    path('', api_views.ShowListView.as_view(), name='show-follow-list'),
]