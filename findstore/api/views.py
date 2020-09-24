from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from . import models, serializers
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

from collections import defaultdict
import pandas as pd
import numpy as np
import surprise
from surprise import SVD
from surprise import Dataset
from surprise.model_selection import cross_validate
from surprise import Reader



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
    recommend = models.Store.objects.all().order_by("-rating")[:10]
    serializer = serializers.StoreSerializer(recommend, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def searchrecommend(request, choice):
    if choice == 'eating':
        store = models.Store.objects.all().filter(Q(address__icontains = request.data['gu']) & Q(address__icontains = request.data['dong']))
    elif choice == 'playing':
        store = models.Store.objects.all().filter(Q(address__icontains = request.data['gu']) & Q(address__icontains = request.data['dong']))
    else:
        return Response()
    if request.data['selected'] == '카테고리':
        store = store.filter(category__icontains = request.data['keyword'])
    else:
        store = store.filter(name__icontains = request.data['keyword'])
    store = store.order_by('-rating')[:10]
    serializer = serializers.StoreSerializer(store, many=True)


def get_top_n(predictions, n=10):

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

@api_view(['GET'])
def reviewcreate(request):
    serializer = serializers.TestReviewsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def testreview(request,store_id):
    serializer = serializers.TestReviewsSerializer(data=request.data)
    qs = models.TestReviews.objects.all()
    qs2 = models.Reviews.objects.all()
    q1 = qs.values('res_id', 'user_name','rating')
    q2 = qs2.values('res_id', 'user_name','rating')
    df1 = pd.DataFrame.from_records(q1)
    df2 = pd.DataFrame.from_records(q2)
    print(df1)
    print(df2)
    df = pd.concat([df1,df2]).reset_index()
    print(df)

    # Load the dataset (download it if needed)
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(df[["user_name","res_id","rating"]],reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)

    # Than predict ratings for all pairs (u, i) that are NOT in the training set.
    # testset = trainset.build_full_trainset()
    testset = trainset.build_anti_testset()
    predictions = algo.test(testset)

    top_n = get_top_n(predictions, n=10)

    # Print the recommended items for each user
    for uid, user_ratings in top_n.items():
        if uid == store_id:
            print(user_ratings)
    
    return Response(serializer.data)