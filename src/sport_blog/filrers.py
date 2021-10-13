import django_filters

from sport_blog.models import Book, Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title', 'description']


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author']
