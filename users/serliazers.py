from rest_framework import serializers
from users.models import Payment

class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'