import random
from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = Faker()
        cnt_authors = 0
        for _ in range(int(input('Number of Authors: '))):
            Author(name=f.name(), email=f.email(), age=random.randint(1, 100)).save()
            cnt_authors += 1
        print(f'Created: {cnt_authors} "AUTHORS"')
