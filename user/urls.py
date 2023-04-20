from rest_framework import routers
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.viewsets import RegisterViewSet, UserViewSet

user_router = routers.DefaultRouter()

user_router.register(r'register', RegisterViewSet, basename='register')
user_router.register(r'', UserViewSet, basename='users')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(user_router.urls))
]
