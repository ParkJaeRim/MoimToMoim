from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        fields = ('id', 'title', 'user','comments', 'content', 'created_at','updated_at')


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = ('id','title','content','created_at','updated_at','user',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    class Meta:
        model = Comment
        fields = ('content','user','article','created_at','updated_at','id')
