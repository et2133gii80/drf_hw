from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    course_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Название')
    preview = models.ImageField(upload_to='course/course_preview/', blank=True, null=True, verbose_name='Превью')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Название')
    preview = models.ImageField(upload_to='course/lesson_preview/', blank=True, null=True, verbose_name='Превью')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    url = models.URLField(blank=True, null=True, verbose_name='Ссылка')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='lessons')
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.course}, {self.user}'



