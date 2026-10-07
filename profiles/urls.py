from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.ProfileView.as_view(), name='profile'),
]