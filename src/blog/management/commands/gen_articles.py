from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Article


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        f = Faker()
        cnt_articles = 0
        for _ in range(int(input('Enter the number of articles: '))):
            Article(title=f.name(), description=f.random_letters(), content=f.text()).save()
            cnt_articles += 1
        print(f'Created {cnt_articles} "ARTICLES"')
