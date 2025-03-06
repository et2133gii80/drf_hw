from tkinter.font import names

from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .views import CourseViewSet

app_name = 'course'


router = DefaultRouter
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns =[
    path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', views.LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson-delete')
             ] + router.urls