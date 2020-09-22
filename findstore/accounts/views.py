from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from knox.models import AuthToken
from rest_framework.authentication import TokenAuthentication
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer, UserUpdateSerializer, UserDeleteSerializer
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .models import User


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        # if len(request.data["username"]) < 6 or len(request.data["password"]) < 4:
            # body = {"message": "short field"}
            # return Response(body, status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": CreateUserSerializer(
                    user, context=self.get_serializer_context()
                ).data
            }
        )


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "uid": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class UpdateAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user

# class DeleteAPI(generics.RetrieveDestroyAPIView):
#     article = get_object_or_404(User, username = article_username)
#     queryset = User.objects.all()
#     serializer_class = UserDeleteSerializer

@api_view(['GET'])
def DeleteUser(request, username):
    user = get_object_or_404(User, username=username)
    # print(user)
    user.delete()
    return Response()

