from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}

class Course (models.Model):
    """
    Класс модель - Курс
    """
    name = models.CharField(max_length=200, verbose_name='Название')
    preview = models.ImageField(upload_to='main/course/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='курс'
        verbose_name_plural='курсы'
        ordering = ('name',)

class Lesson(models.Model):
    """
    Модель описывающее - Урок
    """
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='main/lesson/', verbose_name='Превью', **NULLABLE)
    link_video = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Название курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='урок'
        verbose_name_plural='уроки'
        ordering = ('name',)


class Payment(models.Model):
    """
    Модель для способа оплаты курса или урока
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    date_payment = models.DateField(auto_now_add=True, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(verbose_name='способ оплаты', **NULLABLE) # наличные или перевод на счет.
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')

    id_intent = models.CharField(max_length=300, verbose_name='id_намерение платежа', **NULLABLE)
    id_method = models.CharField(max_length=300, verbose_name='id_метод платежа', **NULLABLE)
    status = models.CharField(max_length=50, verbose_name='статус платежа', **NULLABLE)

    def __str__(self):
        return f'{self.user} {self.date_payment} {self.paid_course} {self.payment_amount}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'

class Subscription(models.Model):
    """
    Подписка на курс для пользователя.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Подписка на курс', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='признак подписки')
    version = models.CharField(max_length=50, default=1, verbose_name='версия подписки')

    def __str__(self):
        return f'Подписка на курс {self.course} ({self.user})'

    class Meta:
        verbose_name='Подписка'
        verbose_name_plural='Подписки'
        ordering = ('user', 'course',)

    def delete(self, **kwargs):
        """Отключение подписки"""
        self.is_active = False
        self.save()

    def update_version(self, version):
        self.version = version
        self.save()

    def activate(self):
        self.is_active = True
        self.save()