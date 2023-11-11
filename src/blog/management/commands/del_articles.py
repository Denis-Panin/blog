from django.core.management.base import BaseCommand
from blog.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        cnt_articles = 0
        articles = Article.objects.all()
        for article in articles:
            article.delete()
            print(article.title)
            cnt_articles += 1
        print(f'Deleted {cnt_articles} "ARTICLES"')
