from django.core.management.base import BaseCommand
from blog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        cnt_categories = 0
        categories = Category.objects.all()
        for category in categories:
            category.delete()
            print(category.name)
            cnt_categories += 1
        print(f'Deleted {cnt_categories} "CATEGORIES"')
