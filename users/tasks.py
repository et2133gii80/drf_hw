from datetime import timedelta
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils import timezone
from rest_framework.generics import get_object_or_404
import os
from course.models import Subscription, Course
import datetime

from users.models import User


@shared_task
def check_inactive_users():
    today = timezone.now().date()
    inactive_date = today - datetime.timedelta(days=30)
    inactive_users = User.objects.filter(
    is_active=False,
    is_staff=False,
    is_superuser=False,
    last_login__isnull=False,
    last_login__lt=inactive_date).update(is_active=False)

    for user in inactive_users:
        if user.last_login__lt >= 30:
            user.save()


@shared_task
def sub_update(pk):
    course = get_object_or_404(Course, pk=pk)
    subscriptions = Subscription.objects.filter(course=course)
    subscribers = [subscription.user for subscription in subscriptions]
    for subscriber in subscribers:
        try:
            send_mail(
                subject="Подписка на курс",
                message=f'Курс "{course.name}" был обновлен',
                from_email=os.getenv('EMAIL_HOST_USER'),
                recipient_list=[subscriber,],
                fail_silently=False,
            )
        except Exception as e:
            print(str(e))