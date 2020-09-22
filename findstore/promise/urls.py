from django.urls import path
from . import views

app_name = 'promise'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('detail/<m_id>', views.detail, name='detail'),
    path('list', views.promiselist, name='promiselist'),
]