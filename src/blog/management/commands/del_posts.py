from django.core.management.base import BaseCommand
from blog.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        cnt_posts = 0
        posts = Post.objects.all()
        for post in posts:
            post.delete()
            print(post.title)
            cnt_posts += 1
        print(f'Deleted {cnt_posts} "POSTS"')
