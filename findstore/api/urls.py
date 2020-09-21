from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register(r"stores", views.StoreViewSet, basename="stores")

urlpatterns = router.urls

app_name = 'api'

urlpatterns = [
    path('store/<store_id>', views.storedetail, name='storedetail'),
]