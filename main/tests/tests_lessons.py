from rest_framework import status
from users.models import User
from rest_framework.test import APITestCase, APIClient


class LessonsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@yandex.ru',
            first_name='Test',
            last_name='Test',
            is_staff=True,
            is_superuser=False
        )

        self.user.set_password('0000')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.url_lessons = '/lessons/'
        self.url_course = '/courses/'

    def test_create_lessons(self):
        """Тест создания модели Lessons"""

        data = {
            'name': 'course_test',
            'description': 'test test'
        }
        response_course = self.client.post(self.url_course, data=data)

        response_lessons = self.client.post(f'{self.url_lessons}create/',
                                            {'course': 4, 'name': 'lessons_test', 'description': 'test test',
                                             'owner': 4, 'link': 'youtube.com'})
        self.assertEqual(response_lessons.status_code, status.HTTP_201_CREATED)
        response_lessons_valid_link = self.client.post(f'{self.url_lessons}create/',
                                                       {'course': 4, 'name': 'lessons_test',
                                                        'description': 'test test',
                                                        'owner': 4, 'link': 'rutube.com'})
        self.assertEqual(response_lessons_valid_link.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_lessons(self):
        """Тест detail модели Lessons"""
        data = {
            'name': 'course_test',
            'description': 'test test'
        }
        response_course = self.client.post(self.url_course, data=data)

        response_lessons = self.client.post(f'{self.url_lessons}create/',
                                            {'course': 5, 'name': 'lessons_test', 'description': 'test test',
                                             'owner': 5, 'link': 'youtube.com'})
        response = self.client.get(f'{self.url_lessons}2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': 2, 'name': 'lessons_test', 'image': None, 'description': 'test test',
                          'link': 'youtube.com', 'course': 5, 'owner': 5})