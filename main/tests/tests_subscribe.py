from rest_framework import status
from users.models import User
from rest_framework.test import APITestCase, APIClient


class SubscribeTestCase(APITestCase):
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
        self.url_course = '/courses/'
        self.url_subscribe = '/subscriptions'

    def test_subscribe_create(self):
        """Тест на создание subscribe"""

        data_course = {
            'name': 'course_test',
            'description': 'test test'
        }
        data_subscribe = {
            'course': 6,
            'is_active': True
        }
        response_course = self.client.post(self.url_course, data=data_course)

        response_subscribe = self.client.post(f'{self.url_subscribe}-create/',
                                              data=data_subscribe)
        print(response_subscribe.json())
        print(response_course.json())
        self.assertEqual(response_subscribe.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_subscribe.json(),
                         {'course': 6, 'id': 1, 'owner': 6, 'is_active': True})

    def test_subscribe_delete(self):
        """Тест на удаление subscribe"""

        data_course = {
            'name': 'course_test',
            'description': 'test test'
        }
        data_subscribe = {
            'course': 7,
            'is_active': True
        }
        response_course_create = self.client.post(self.url_course, data=data_course)

        response_subscribe_create = self.client.post(f'{self.url_subscribe}-create/',
                                              data=data_subscribe)
        response_subscribe_delete = self.client.delete(f'{self.url_subscribe}-delete/2/')
        self.assertEqual(response_subscribe_delete.status_code, status.HTTP_204_NO_CONTENT)