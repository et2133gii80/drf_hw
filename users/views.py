from rest_framework import viewsets, generics

from users.models import Payment
from users.serliazers import PaymentSerializers


# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializers
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
    queryset = Payment.objects.all()
