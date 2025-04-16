from rest_framework import serializers
from users.models import Payment, User

class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):

     class Meta:
         model = User
         fields = '__all__'