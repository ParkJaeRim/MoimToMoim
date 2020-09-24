from rest_framework import serializers
from accounts.serializers import UserSerializer
from api.serializers import StoreSerializer
from .models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Meeting
        # fields = ('id', 'title', 'background_img', 'avg_age', 'ppl', 'user')
        fields = '__all__'
        
class RecommendSerializer(serializers.ModelSerializer):
    store = StoreSerializer(required=False)
    class Meta:
        model = Meeting
        fields = '__all__'