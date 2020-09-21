from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Meeting
        # fields = ('id', 'title', 'background_img', 'avg_age', 'ppl', 'user')
        fields = '__all__'
