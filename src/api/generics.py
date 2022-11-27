from rest_framework import serializers

from blog.models import Author, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'content',
        )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'name',
            'email',
            'age',
        )
