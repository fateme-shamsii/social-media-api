from django.urls import path
from . import api_views
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView

urlpatterns = [
    path('register/', api_views.CreateUserView.as_view(), name='create_user'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]