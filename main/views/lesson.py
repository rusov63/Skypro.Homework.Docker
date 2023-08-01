# CRUD для моделей для урока — Generic.
from rest_framework import filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from main.models import Lesson
from main.seriallizers.lesson import LessonSerializer


class LessonCreateAPIView(CreateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer

class LessonRetrieveAPIView(RetrieveAPIView):
    """Просмотр одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonListAPIView(ListAPIView):
    """Просмотр всех уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # фильтр поиска урока
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    #http://localhost:8000/lessons/?search=Django


class LessonUpdateAPIView(UpdateAPIView):
    """Создание урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(DestroyAPIView):
    """Удаление урока"""
    queryset = Lesson.objects.all()