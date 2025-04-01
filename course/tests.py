from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Lesson, Course
from users.models import User


class LessonUserTestCase(APITestCase):

    def setUp(self):
        #Подготовка данных перед тестом
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(course_name='test_course', owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name='test_lesson', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('course:lesson-get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_name'), 'test_lesson')

    def test_create_lesson(self):
        url = reverse('course:lesson-create')
        data= {
            'lesson_name': 'test_lesson_1',
            'url': 'https://www.youtube.com'

        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_list(self):
        url = reverse('course:lesson-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        url = reverse('course:lesson-update', args=(self.lesson.pk,))
        data = {
            'lesson_name': 'test_lesson_2',
            'url': 'https://www.youtube.com',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_name'), 'test_lesson_2')

    def test_lesson_delete(self):
        url = reverse('course:lesson-delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)








