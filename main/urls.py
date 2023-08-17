from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views.course import CourseViewSet
from main.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView,\
LessonDestroyAPIView
from main.views.payment import *
from main.views.subscription import *

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'), # Создание
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'), # просмотр всех уроков
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'), # просмотр одного урока
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'), # изменение
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'), # удаление

    # payments
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
    path('payment-intent/create/', PaymentIntentCreateView.as_view(), name='payment_intent_create'),
    path('payment-method/confirm/', PaymentIntentConfirmView.as_view(), name='payment_method_confirm'),
    #path('payments/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    #path('payments/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment_delete'),

    # Subscription
    path('subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveAPIView.as_view(), name='subscription_retrieve'),
    path('subscriptions/delete/<int:pk>/', SubscriptionDeleteAPIView.as_view(), name='subscription_delete')



] + router.urls



#print(router.urls)
