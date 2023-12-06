from blog.models import Category
from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        f = Faker()
        cnt_category = 0
        for _ in range(int(input('Enter the number of categories: '))):
            Category(name=f.word()).save()
            cnt_category += 1
        print(f'Created {cnt_category} "CATEGORIES"')
