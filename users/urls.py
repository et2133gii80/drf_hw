from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import PaymentViewSet

app_name = 'payments'


router = DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns =[
             ] + router.urls