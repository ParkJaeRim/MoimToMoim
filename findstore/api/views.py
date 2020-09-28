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
    return Response(serializer.data)


@api_view(['GET'])
def reviewcreate(request):
    serializer = serializers.TestReviewsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        testreview(request)
        return Response(serializer.data)

def meetingCreate(meeting_id):
    store_qs = models.Store.objects.all()
    for store in store_qs:
        models.Recommand(user_id=meeting_id,rating=store.rating,res_id=store.id,
        address=store.address,name=store.name,category=store.category).save()


def get_top_n(predictions, meeting_id):
    # First map the predictions to each user.
    top_n = defaultdict(list)
    dic = {}
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    for uid, user_ratings in top_n.items():
        if uid==meeting_id:
            for user_rating in user_ratings:
                dic[user_rating[0]] =user_rating[1]
    return dic

def testreview(request):
    meeting_id = str(request.data.get('user_name'))
    qs = models.TestReviews.objects.all()
    qs2 = models.Reviews.objects.all()
    store_qs = models.Store.objects.all()
    q1 = qs.values('res_id', 'user_name','rating')
    q2 = qs2.values('res_id', 'user_name','rating')
    store_q = store_qs.values_list('id','address','name','category')
    store_addr = {}
    for s in store_q:
        store_addr[s[0]] = s[1:]

    df1 = pd.DataFrame.from_records(q1)
    df2 = pd.DataFrame.from_records(q2)
    df = pd.concat([df1,df2]).reset_index()

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

    top_n = get_top_n(predictions,meeting_id)
    # Print the recommended items for each user
    recom_qs = models.Recommand.objects.all().filter(user_id=meeting_id)

    for recom in recom_qs:
        recom.rating = top_n.get(int(recom.res_id))
        recom.save()
    

def resChange(resList):
    res = []
    resNum = resList.split('/')
    for n in resNum:
        try:
            store = get_object_or_404(models.Store, pk=n)
            serializer = serializers.StoreSerializer(store)
            res.append(serializer.data)
        except:
            continue
    return res