from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from . import models, serializers
from accounts.serializers import UserSerializer

from django.contrib.auth import get_user_model


User=get_user_model()


class SmallPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StoreSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        queryset = (
            models.Store.objects.all().filter(store_name__contains=name).order_by("id")
        )
        return queryset


@api_view(['GET'])
def storedetail(request, store_id):
    store = get_object_or_404(models.Store, pk=store_id)
    serializer = serializers.StoreSerializer(store)
    return Response(serializer.data)

@api_view(['GET'])
def storereview(request, store_id):
    reviews = models.Reviews.objects.filter(res_id=store_id)
    serializer = serializers.ReviewsSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def storerecommend(request,store_id): # 랭킹 상위 10위까지
    print("test")
    recommend = models.Store.objects.all().order_by("-rating")[:10]
    serializer = serializers.StoreSerializer(recommend, many=True)
    return Response(serializer.data)

