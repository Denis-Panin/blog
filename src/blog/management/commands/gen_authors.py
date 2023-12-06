import random

from blog.models import Author
from django.core.management.base import BaseCommand
from faker import Faker

GENDER_CHOICES = [
    ('M'),
    ('F'),
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = Faker()
        cnt_authors = 0
        for _ in range(int(input('Number of Authors: '))):
            Author(
                first_name=f.first_name(),
                last_name=f.last_name(),
                email=f.email(),
                age=random.randint(1, 100),
                about_author=f.text() * 5,
                gender=random.choice(GENDER_CHOICES)
            ).save()
            cnt_authors += 1
        print(f'Created: {cnt_authors} "AUTHORS"')
