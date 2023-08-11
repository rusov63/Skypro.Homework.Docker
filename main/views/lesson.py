# CRUD для моделей для урока — Generic.
from rest_framework import filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from main.models import Lesson
from main.paginators import MainPaginator
from main.seriallizers.lesson import LessonSerializer
from main.permissions import IsOwner, IsModerator


class LessonCreateAPIView(CreateAPIView):
    """
    Создание урока
    """
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        # Автоматическое сохранение владельца при создании нового объекта
        new_les = serializer.save()
        new_les.owner = self.request.user
        new_les.save()


class LessonRetrieveAPIView(RetrieveAPIView):
    """
    Просмотр одного урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonListAPIView(ListAPIView):
    """
    Просмотр всех уроков
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]
    pagination_class = MainPaginator

    # фильтр поиска урока
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # http://localhost:8000/lessons/?search=Django


class LessonUpdateAPIView(UpdateAPIView):
    """
    Редактирование урока
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]


class LessonDestroyAPIView(DestroyAPIView):
    """
    Удаление урока
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
