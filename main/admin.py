
from django.contrib import admin

from main.models import Course, Lesson, Payment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date_payment', 'paid_course', 'payment_amount', 'payment_method', 'is_paid')
    search_fields = ('user',)
