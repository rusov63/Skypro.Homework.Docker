from django.core.management import BaseCommand

from main.models import Course, Lesson, Payment


class Command(BaseCommand):
    """Класс, который удаляет данные из модели - Course, Lesson, Payment"""

    def handle(self, *args, **options):
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()
