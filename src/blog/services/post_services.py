from blog.models import Post


def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
