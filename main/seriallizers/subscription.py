from rest_framework import serializers

from main.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализатор представление модели Подписка
    """

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'course', ]