import django_filters

from blog.models import Article, Book


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ['title', 'description']


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category']
