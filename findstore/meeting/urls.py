from django.urls import path
from . import views

app_name = 'meeting'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('indvcreate/', views.Indvcreate, name='Indvcreate'),

    path('detail/<m_id>', views.detail, name='detail'),
    path('modify/<m_id>', views.modify, name='modify'),
    path('delete/<m_id>', views.delete, name='delete'),

]