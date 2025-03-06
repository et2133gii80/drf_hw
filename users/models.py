from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='номер телефона')
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name='страна')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


