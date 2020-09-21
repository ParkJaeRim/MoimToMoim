from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer, CommentSerializer
from accounts.serializers import UserSerializer

from django.contrib.auth import get_user_model


User=get_user_model()


@api_view(['GET'])
def index(request):
    articles = Article.objects.all().order_by('-pk')
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)


@api_view(['GET'])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['GET','POST'])
# @api_view(['GET'])
@permission_classes([IsAuthenticated])
def modify(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user != article.user:
        return Response()

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        temp = serializer.initial_data
        article.title = temp['title']
        article.content = temp['content']
        article.save()
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.user:
        article.delete()
    return Response()


@api_view(['GET'])
def comments(request, article_pk):
    target_article = get_object_or_404(Article, pk=article_pk)
    comment = Comment.objects.filter(article = target_article)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    target_article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=target_article, user=request.user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user and comment.article==article:
        comment.delete()
    return Response()



@api_view(['GET'])
def get_user_articles(request, user_name):
    user = get_object_or_404(User,username=user_name)
    article = Article.objects.filter(user=user)

    serializer = ArticleSerializer(article,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_user_comments(request, user_name):
    user = get_object_or_404(User,username=user_name)
    comment = Comment.objects.filter(user=user)

    serializer = CommentSerializer(comment,many=True)

    return Response(serializer.data)