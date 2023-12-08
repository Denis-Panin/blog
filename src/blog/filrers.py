from blog.models import Article, Book
from django import forms
import django_filters


class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form_body_item_input',
            'placeholder': 'title'
        }),
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form_body_item_input',
            'placeholder': 'description'
        }),
    )
    content = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form_body_item_input',
            'placeholder': 'content'
        }),
    )

    class Meta:
        model = Article
        fields = ['title', 'description', 'content']


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category']
