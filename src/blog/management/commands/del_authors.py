from blog.models import Author
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        cnt_authors = 0
        authors = Author.objects.all()
        for author in authors:
            author.delete()
            print(f'{author.first_name} - {author.email}')
            cnt_authors += 1
        print(f'Deleted: {cnt_authors} "AUTHORS"')
