from rest_framework import viewsets, generics

from users.models import Payment, User, Donation
from users.serliazers import PaymentSerializers, UserSerializers, DonationSerializers
from users.services import create_stripe_price, create_stripe_session


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


class DonationCreateAPIView(generics.CreateAPIView):
    serializer_class = DonationSerializers
    queryset = Donation.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount = payment.amount
        price = create_stripe_price(amount)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()
