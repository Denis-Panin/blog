from .models import Article, Category


def get_new_articles():
    return Article.objects.all().order_by('-created')[0:3]


def get_all_categories():
    return Category.objects.all().only('name')
