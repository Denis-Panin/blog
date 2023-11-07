from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Post


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        f = Faker()
        cnt_posts = 0
        for _ in range(int(input('Enter the number of posts: '))):
            Post(title=f.name(), description=f.random_letters(), content=f.text()).save()
            cnt_posts += 1
        print(f'Created {cnt_posts} "POSTS"')
