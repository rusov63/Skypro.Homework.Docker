from rest_framework import generics, filters

from main.models import Payment
from main.seriallizers.payment import PaymentSerializer

"""Представление CRUD"""

class PaymentCreateAPIView(generics.CreateAPIView):
    """Создание платежа"""
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """Просмотр всех платежей"""
    serializer_class =  PaymentSerializer
    queryset = Payment.objects.all()

    # сортировка по дате оплаты.
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date_payment']
    #http://localhost:8000/payments/?ordering=date_payment
    #http://localhost:8000/payments/?ordering=-date_payment

    # фильтр по способу оплаты.
    search_fields = ['payment_method']
    #http://localhost:8000/payments/?search=наличные
    #http://localhost:8000/payments/?search=перевод на счет

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр одного платежа"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentUpdateAPIView(generics.UpdateAPIView):
    """Изменение платежа"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentDeleteAPIView(generics.DestroyAPIView):
    """Удаление платежа"""
    queryset = Payment.objects.all()


