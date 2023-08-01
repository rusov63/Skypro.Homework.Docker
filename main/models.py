from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}

class Course (models.Model):
    """Класс модель - Курс"""
    name = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='main/course/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='курс'
        verbose_name_plural='курсы'
        ordering = ('name',)

class Lesson(models.Model):
    """Модель описывающее - Урок"""
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='main/lesson/', verbose_name='Превью', **NULLABLE)
    link_video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='урок'
        verbose_name_plural='уроки'
        ordering = ('name',)


class Payment(models.Model):
    """Модель описывающий - Платеж"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    date_payment = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='способ оплаты', **NULLABLE) # наличные или перевод на счет.
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')

    def __str__(self):
        return f'{self.user} {self.date_payment} {self.paid.course} {self.payment_amount}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
