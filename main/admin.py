from django.contrib import admin

from main.models import Course, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'user',)
#     search_fields = ('name',)
#
# @admin.register(Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'user',)
#     search_fields = ('name',)