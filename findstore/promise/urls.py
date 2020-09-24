from django.urls import path
from . import views

app_name = 'promise'

urlpatterns = [
    path('<int:meeting_id>/', views.promiselist, name='promiselist'),
    path('<int:meeting_id>/create/', views.create, name='create'),
    path('detail/<int:promise_id>', views.detail, name='detail'),
    path('<str:user_name>/list/', views.userpromiselist,name='userpromiselist')
]