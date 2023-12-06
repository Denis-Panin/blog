from blog.models import Article, Book
import django_filters


class ArticleFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ['title', 'description']


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category']
