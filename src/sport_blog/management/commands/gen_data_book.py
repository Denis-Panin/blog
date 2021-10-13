import random

from django.core.management.base import BaseCommand
from faker import Faker

from sport_blog.models import Author, Book, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(5):
            Author(name=fake.name(), email=fake.email(), age=random.randint(1, 100)).save()

        for _ in range(5):
            Category(name=fake.company()).save()

        for i in range(10):
            author = Author.objects.order_by('?').last()
            category = Category.objects.order_by('?').last()
            Book(title=f'title{i}', author=author, category=category).save()
