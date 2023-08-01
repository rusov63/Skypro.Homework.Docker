from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Payment, Course


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор представление модели Платежи"""

    # название курса вместо цифры
    paid_course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())

    class Meta:
        model = Payment
        fields = ['id', 'user', 'date_payment', 'paid_course', 'payment_amount', 'payment_method', 'is_paid']