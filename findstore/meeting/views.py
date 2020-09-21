from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Meeting
from .serializers import MeetingSerializer
from accounts.serializers import UserSerializer

from django.contrib.auth import get_user_model


User=get_user_model()


@api_view(['GET'])
def index(request):
    meetings = Meeting.objects.all().order_by('-pk')
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = MeetingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, m_id):
    meeting = get_object_or_404(Meeting, pk = m_id)
    serializer = MeetingSerializer(meeting)
    return Response(serializer.data)




# @api_view(['GET','POST'])
# # @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def modify(request, article_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     if request.user != article.user:
#         return Response()

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         temp = serializer.initial_data
#         article.title = temp['title']
#         article.content = temp['content']
#         article.save()
#     return Response()


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def delete(request, article_id):
#     article = get_object_or_404(Article, id=article_id)
#     if request.user == article.user:
#         article.delete()
#     return Response()