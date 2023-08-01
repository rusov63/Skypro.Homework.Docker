from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Lesson"""

    # название курса вместо цифры (читать комментарий GET_lessons_README.txt).
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'course', 'user']
