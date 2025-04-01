from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

from course.models import Course, Lesson


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='номер телефона')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='страна')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    payment_amount = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True,)





