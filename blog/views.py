from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from . import models
from . import serializers

from .models import BlogPost, Author
from .permissions import IsOwner
from .serializers import AuthorPostsSerializer, PostSerializer


class BlogPostViewset(viewsets.ModelViewSet):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_fields = ('author', 'title')


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.Author.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_fields = ('id', 'name', 'email')


class UserPostsView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request, user_id):
        posts = BlogPost.objects.all().filter(author=user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class UserProfileView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request, name):
        user = get_object_or_404(Author.objects.all(), name=name)
        serializer = AuthorPostsSerializer(user)
        return Response(serializer.data)
