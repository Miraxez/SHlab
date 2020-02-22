from rest_framework import viewsets
from . import models
from . import serializers


class BlogPostNewViewset(viewsets.ModelViewSet):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_fields = ('author', 'title')


class UserViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.UsersSerializer
    filterset_fields = ('id', 'name', 'email')
