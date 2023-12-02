from .models import Article, Author, Category
from django.db.models import Count


def get_new_articles():
    return Article.objects.all().order_by('-created')[:3]


def get_all_categories():
    return Category.objects.all().only('name')


def get_top_authors():
    authors = Author.objects.annotate(article_count=Count('articles'))
    sorted_authors = sorted(authors, key=lambda x: x.article_count, reverse=True)[:3]
    return sorted_authors
