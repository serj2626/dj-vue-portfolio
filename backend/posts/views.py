from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


class PostListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
