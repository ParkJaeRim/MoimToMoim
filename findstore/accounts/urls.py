from django.urls import path, include
from .views import RegistrationAPI, LoginAPI, UserAPI, UpdateAPI, DeleteAPI

app_name='accounts'
urlpatterns = [
    path("register/", RegistrationAPI.as_view()),
    path("login/", LoginAPI.as_view()),
    path("user/", UserAPI.as_view()),
    path("update/", UpdateAPI.as_view()),
    path("delete/<int:pk>", DeleteAPI.as_view()),
]