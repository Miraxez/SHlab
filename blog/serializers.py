from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'description', 'body', 'author']


class AuthorPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'posts']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
