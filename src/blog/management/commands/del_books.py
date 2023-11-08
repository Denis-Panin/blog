from django.core.management.base import BaseCommand
from blog.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        cnt_books = 0
        books = Book.objects.all()
        for book in books:
            book.delete()
            print(book.title)
            cnt_books += 1
        print(f'Deleted {cnt_books} "BOOKS"')
