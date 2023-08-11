from rest_framework import generics, filters

from main.models import Subscription
from main.seriallizers.subscription import SubscriptionSerializer

"""Представление CRUD для модели Подписка"""

class SubscriptionCreateAPIView(generics.CreateAPIView):
    """
    Создание пидписки
    """
    serializer_class = SubscriptionSerializer


class SubscriptionListAPIView(generics.ListAPIView):
    """
    Просмотр всех подписок
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одной подписки
    """
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class SubscriptionDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление подписки
    """
    queryset = Subscription.objects.all()


