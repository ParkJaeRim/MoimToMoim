from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Meeting
from .serializers import MeetingSerializer
from accounts.serializers import UserSerializer
from api.views import meetingCreate
from django.contrib.auth import get_user_model


User=get_user_model()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    meetings = Meeting.objects.all().order_by('-pk')
    # meetingss = Meeting.objects.filter(user = request.user)
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = MeetingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        meeting = Meeting.objects.all().last()
        meetingCreate(meeting.id)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Indvcreate(request):
    print(request)
    serializer = MeetingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, m_id):
    meeting = get_object_or_404(Meeting, pk = m_id)
    serializer = MeetingSerializer(meeting)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def modify(request, m_id):
    meeting = get_object_or_404(Meeting, pk=m_id)
    serializer = MeetingSerializer(data=request.data)
    temp = serializer.initial_data
    meeting.title = temp['title']
    meeting.content = temp['background_img']
    meeting.save()
    return Response()


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def delete(request, m_id):
    meeting = get_object_or_404(Meeting, id=m_id)
    # if request.user == article.user:
    meeting.delete()
    return Response()