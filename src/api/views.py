from api.generics import AuthorSerializer, ArticleSerializer
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from blog.models import Article, Author


class ArticleAPIViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 4


class ArticleAPIViewSet2(generics.GenericAPIView):
    queryset = Article.objects.all().order_by('-id')

    def get(self, request):
        res = Article.objects.all().order_by('-id')
        ser = ArticleSerializer(res, many=True)
        return Response(ser.data)


class AuthorAPIView(generics.GenericAPIView):
    queryset = Author.objects.all().order_by('-id')

    def get(self, request):
        res = Author.objects.all().order_by('-id')
        ser = AuthorSerializer(res, many=True)
        return Response(ser.data)
