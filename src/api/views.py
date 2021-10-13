from api.generics import AuthorSerializer, PostSerializer
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from sport_blog.models import Author, Post


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 4


class PostAPIViewSet2(generics.GenericAPIView):
    queryset = Post.objects.all().order_by('-id')

    def get(self, request):
        res = Post.objects.all().order_by('-id')
        ser = PostSerializer(res, many=True)
        return Response(ser.data)


class AuthorAPIView(generics.GenericAPIView):
    queryset = Author.objects.all().order_by('-id')

    def get(self, request):
        res = Author.objects.all().order_by('-id')
        ser = AuthorSerializer(res, many=True)
        return Response(ser.data)
