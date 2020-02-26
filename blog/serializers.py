from rest_framework import serializers
from .models import BlogPost, Author


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'description', 'body', 'author', 'owner']


class AuthorPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'email', 'posts']


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'owner']
