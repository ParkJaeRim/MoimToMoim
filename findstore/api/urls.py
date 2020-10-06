from os import name
from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register("stores", views.StoreViewSet, basename="stores")

urlpatterns = router.urls

app_name = 'api'

urlpatterns = [
    path('store/<int:store_id>', views.storedetail, name='storedetail'),

    path('store/reviews/test/<store_id>', views.testreview, name='testreview'),
    path('store/review2/create/', views.reviewcreate, name='reviewcreate'),
    path('store/firstrecommend/<store_id>', views.storerecommend, name='storerecommend'),
    
    path('store/storerecommend/<str:choice>/<int:meeting_id>', views.searchrecommend, name='searchrecommend'),
    path('hotplace/', views.hotplace, name='hotplace'),
]