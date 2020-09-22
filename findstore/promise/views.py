from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Promise
from meeting.models import Meeting
from .serializers import PromiseSerializer
from accounts.serializers import UserSerializer

from django.contrib.auth import get_user_model


User=get_user_model()


@api_view(['GET'])
def promiselist(request, meeting_id):
    target_meeting = get_object_or_404(Meeting, id=meeting_id)
    promises = Promise.objects.filter(meeting = target_meeting)
    serializer = PromiseSerializer(promises, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request, meeting_id):
    target_meeting = get_object_or_404(Meeting, id=meeting_id)
    serializer = PromiseSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(meeting=target_meeting, user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, m_id):
    promise = get_object_or_404(Promise, pk = m_id)
    serializer = PromiseSerializer(promise)
    return Response(serializer.data)