from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views.course import CourseViewSet
from main.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView,\
LessonDestroyAPIView
from main.views.payment import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentUpdateAPIView, \
PaymentDeleteAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'), # Создание
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'), #
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'), # один урок
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'), # изменение
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'), # удаление

    # payments
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
    path('payments/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('payments/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment_delete'),
] + router.urls



#print(router.urls)
