from django.core.management import BaseCommand
from users.models import User
import os

# Создание модератора с флагом. if_staff = True

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator@mail.ru',
            name='moderator',
            is_staff=True,
            is_superuser=False

        )

        user.set_password('123456')
        user.save()