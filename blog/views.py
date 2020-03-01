from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from . import models
from . import serializers

from .models import BlogPost
from .permissions import IsOwner
from .serializers import AuthorPostsSerializer, PostSerializer, UserSerializer


class BlogPostViewset(viewsets.ModelViewSet):
    permission_classes = [IsOwner, IsAuthenticated]
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_fields = ('title', 'author',)


class UserPostsView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request, user_id):
        posts = BlogPost.objects.all().filter(owner_id=user_id)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class UserProfileView(APIView):
    permission_classes = [IsOwner, IsAuthenticated]

    def get(self, request, name):
        user = get_object_or_404(User.objects.all(), username=name)
        serializer = AuthorPostsSerializer(user)
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('id', 'username', 'first_name', 'last_name', 'email')
