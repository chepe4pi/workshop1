from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from orders.models import Order


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class OrderSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ('name', 'user', 'value')
