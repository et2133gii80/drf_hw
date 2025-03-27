from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import PaymentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'payments'


router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns =[path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              path('user/create/', views.UserCreateAPIView.as_view(), name='user-create'),
              path('user/', views.UserListAPIView.as_view(), name='user-list'),
              path('user/<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user-get'),
              path('user/update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
              path('user/delete/<int:pk>/', views.UserDestroyAPIView.as_view(), name='user-delete')
             ] + router.urls