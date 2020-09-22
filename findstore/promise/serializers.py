from rest_framework import serializers
from accounts.serializers import UserSerializer
from api.serializers import StoreSerializer
from .models import Promise


class PromiseSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Promise
        fields = '__all__'