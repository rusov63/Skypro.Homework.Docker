from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Lesson
from main.seriallizers.lesson import LessonSerializer


# class CarApiTestCase(APITestCase):
#
#     def test_get_moto_list(self):
#         id_1 = Lesson.objects.create(title='test', description='2023', year=2007)
#         url = reverse('vehicle:moto_list')
#         response = self.client.get(url)
#         serializer_data = LessonSerializer([id_1]).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data)
#
#     def test_get_moto_retrieve(self):
#         url = reverse('vehicle:moto_retrieve<int:pk>')
#         response = self.client.get(url)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)


class LessonSerializers(APITestCase):

    def test_lessonSerializers(self):
        less_1 = Lesson.objects.create(name='test')
        less_2 = Lesson.objects.create(name='test2')
        data = LessonSerializer([less_1, less_1], many=True).data
        expected_data = [
            {
                'id': less_1.id,
                'name': 'test',
            },
            {
                'id': less_1.id,
                'name': 'test2',
            }
        ]
        self.assertEqual(expected_data, data)
