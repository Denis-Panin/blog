from blog.models import Article, Author, Category
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        f = Faker()
        cnt_articles = 0
        for _ in range(int(input('Enter the number of articles: '))):
            author = Author.objects.order_by('?').last()
            category = Category.objects.order_by('?').last()
            (Article(
                title=f'article title № {cnt_articles}',
                description=f.words(),
                content=f.text() * 4,
                author=author,
                category=category
            ).save())
            cnt_articles += 1
        print(f'Created {cnt_articles} "ARTICLES"')
