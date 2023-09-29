from django.urls import path
from apps.users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', views.RegisterUserView.as_view(), name='register-user'),
    path('list', views.ListUserView.as_view(), name='list-user'),
    path('authenticate', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
