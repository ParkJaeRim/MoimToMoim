from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Promise
from meeting.models import Meeting
from .serializers import PromiseSerializer
from accounts.serializers import UserSerializer
from api.views import resChange

from django.contrib.auth import get_user_model


User=get_user_model()


@api_view(['GET'])
def promiselist(request, meeting_id):
    target_meeting = get_object_or_404(Meeting, id=meeting_id)
    promises = Promise.objects.filter(meeting = target_meeting)
    serializer = PromiseSerializer(promises, many=True)
    asd = []
    for i in range(len(serializer.data)):
        reslist = resChange(serializer.data[i]['storelist'])
        newdict = {'reslist': reslist}
        newdict.update(serializer.data[i])
        asd.append(newdict)
    return Response(asd)

@api_view(['GET'])
def userpromiselist(request, user_name):
    target_user = get_object_or_404(User, username=user_name)  # 유저는 외래키로 일단 담아놔 
    print(target_user)
    # promises = Promise.objects.all() # 앞에는 칼럼명 뒤에는 내가 보내주는거 변수명
    promises = Promise.objects.filter(user_id = target_user) # 앞에는 칼럼명 뒤에는 내가 보내주는거 변수명
    print(promises)
    serializer = PromiseSerializer(promises, many=True)
    asd = []
    for i in range(len(serializer.data)):
        reslist = resChange(serializer.data[i]['storelist'])
        newdict = {'reslist': reslist}
        newdict.update(serializer.data[i])
        asd.append(newdict)
    return Response(asd)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request, meeting_id):
    target_meeting = get_object_or_404(Meeting, id=meeting_id)
    serializer = PromiseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(meeting=target_meeting, user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, promise_id):
    target_promise = get_object_or_404(Promise, id=promise_id)
    serializer = PromiseSerializer(target_promise)
    reslist = resChange(serializer.data['storelist'])
    newdict = {'reslist': reslist}
    newdict.update(serializer.data)
    return Response(newdict)


@api_view(['POST'])
def updatepromise(request, promise_id):
    promise = get_object_or_404(Promise, id=promise_id)
    serializer = PromiseSerializer(data=request.data)
    temp = serializer.initial_data
    promise.storelist = temp['storelist']
    promise.isfinish = temp['isfinish']
    promise.save()
    return Response()


@api_view(['POST'])
def deleteprimise(request, promise_id):
    promise = get_object_or_404(Promise, id=promise_id)
    promise.delete()
    return Response()



