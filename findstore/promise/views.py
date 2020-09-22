from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Promise
from .serializers import PromiseSerializer
from accounts.serializers import UserSerializer

from django.contrib.auth import get_user_model


User=get_user_model()


@api_view(['GET'])
def index(request):
    promises = Promise.objects.all().order_by('-pk')
    serializer = PromiseSerializer(promises, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = PromiseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, m_id):
    promise = get_object_or_404(Promise, pk = m_id)
    serializer = PromiseSerializer(promise)
    return Response(serializer.data)

@api_view(['GET'])
def promiselist(request):
    promise = Promise.objects.all()[:10]
    serializer = PromiseSerializer(promise,many=True)
    return Response(serializer.data)