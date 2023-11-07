from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Author, Book, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = Faker()
        cnt_books = 0
        for _ in range(int(input('Number of books: '))):
            author = Author.objects.order_by('?').last()
            category = Category.objects.order_by('?').last()
            Book(title=f.random_letters(), author=author, category=category).save()
            cnt_books += 1
        print(f'Created: {cnt_books} "BOOKS"')

