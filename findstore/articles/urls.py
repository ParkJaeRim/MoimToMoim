from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/modify/', views.modify, name='modify'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    
    path('<int:article_pk>/comments/', views.comments, name='comments'),
    path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:article_id>/comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    
    path('<str:user_name>/articles/', views.get_user_articles, name='get_user_articles'),
    path('<str:user_name>/comments/', views.get_user_comments, name='get_user_comments'),
]