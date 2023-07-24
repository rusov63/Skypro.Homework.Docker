from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}

class Course (models.Model):
    """Класс модель - Курс"""
    name = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='main/course/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='курс'
        verbose_name_plural='курсы'


class Lesson(models.Model):
    """Модель описывающее - Урок"""
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='main/lesson/', verbose_name='Превью', **NULLABLE)
    link_video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='урок'
        verbose_name_plural='уроки'


