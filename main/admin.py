from django.contrib import admin

from main.models import Course, Lesson, Payment, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Админ панель. Отображение модели Курсы
    """
    list_display = ('name', 'description',)
    search_fields = ('name',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Админ панель. Отображение модели Уроки
    """
    list_display = ('name', 'description',)
    search_fields = ('name',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """
    Админ панель. Отображение модели Оплаты
    """
    list_display = ('date_payment', 'paid_course', 'payment_amount', 'payment_method', 'is_paid')
    search_fields = ('user',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    Админ панель. Отображение модели Подписки
    """
    list_display = ('user', 'course')
    search_fields = ('user', 'course',)
