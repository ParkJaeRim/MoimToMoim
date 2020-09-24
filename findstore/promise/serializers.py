from rest_framework import serializers

from accounts.serializers import UserSerializer
from meeting.serializers import MeetingSerializer

from .models import Promise
from meeting.models import Meeting


class PromiseSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    meeting = MeetingSerializer(required=False)
    class Meta:
        model = Promise
        fields = '__all__'