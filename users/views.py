from rest_framework import viewsets, generics

from users.models import Payment, User
from users.serliazers import PaymentSerializers, UserSerializers


# Create your views here.

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializers
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method',)
    ordering_fields = ('payment_date',)
    queryset = Payment.objects.all()

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
