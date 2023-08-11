from rest_framework import status
from users.models import User
from rest_framework.test import APITestCase, APIClient


class CourseTestCase(APITestCase):
    """Тесты модели Course"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Test',
            last_name='Test',
            is_staff=False,
            is_superuser=False
        )

        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.url_course = '/courses/'

    def test_create_course(self):
        """Тест создания модели Course"""
        data = {
            'name': 'course_test',
            'description': 'test test'
        }
        response = self.client.post(self.url_course, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_course(self):
        """Тест деталей модели Course"""
        self.test_create_course()
        response = self.client.get(f'{self.url_course}2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 2, 'lesson_count': 0, 'lessons': [], 'subscribe': [], 'name': 'course_test',
                          'image': None, 'description': 'test test', 'price': 0, 'owner': 2})

    def test_list_course(self):
        """Тест листа модели Course"""
        self.test_create_course()
        response = self.client.get(self.url_course)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'count': 1, 'next': None, 'previous': None, 'results': [
                             {'id': 3, 'lesson_count': 0, 'lessons': [], 'subscribe': [], 'name': 'course_test',
                              'image': None, 'description': 'test test', 'price': 0, 'owner': 3}]}
                         )