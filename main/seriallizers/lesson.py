from rest_framework import serializers
from main.models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Lesson"""
    class Meta:
        model = Lesson
        fields = '__all__'