from django_filters.rest_framework import filters
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost, Author
from .serializers import BlogPostSerializer, UserSerializer, UserPostsSerializer, AuthorPostsSerializer, PostSerializer


class BlogPostView(APIView):

    def post(self, request):
        blogpost = request.data.get('blogpost')
        # Create an article from the above data
        serializer = BlogPostSerializer(data=blogpost)
        if serializer.is_valid(raise_exception=True):
            blogpost_saved = serializer.save()
        return Response({"success": "Blog post '{}' created successfully".format(blogpost_saved.title)})

    def put(self, request, pk):
        saved_blogpost = get_object_or_404(BlogPost.objects.all(), pk=pk)
        data = request.data.get('blogpost')
        serializer = BlogPostSerializer(instance=saved_blogpost, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            blogpost_saved = serializer.save()
        return Response({
            "success": "Blog post '{}' updated successfully".format(blogpost_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        blogpost = get_object_or_404(BlogPost.objects.all(), pk=pk)
        blogpost.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)

    def get(self, request, pk):
        # Get object with this pk
        blogpost = get_object_or_404(BlogPost.objects.all(), pk=pk)
        serializer = BlogPostSerializer(blogpost)
        return Response({"blogpost": serializer.data})


class BlogPostArrayView(APIView):
    def get(self, request):
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(posts, many=True)
        return Response({"posts": serializer.data})


class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(Author.objects.all(), name=username)
        authorid = getattr(user, 'id')
        return BlogPost.objects.filter(author_id=authorid)


class UsersView(APIView):
    def get(self, request):
        users = Author.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})


class UserView(APIView):
    def get(self, request, name):
        # Get object with this pk
        user = get_object_or_404(Author.objects.all(), name=name)
        serializer = UserSerializer(user)
        return Response({"user": serializer.data})


class UserPostsView(APIView):
    def get(self, request, name):
        # Get object with this pk
        user = get_object_or_404(Author.objects.all(), name=name)
        serializer = UserPostsSerializer(user)
        return Response(serializer.data)


class AuthorPostsView(APIView):
    def get(self, request, name):
        # Get object with this pk
        user = get_object_or_404(Author.objects.all(), name=name)
        serializer = AuthorPostsSerializer(user)
        return Response(serializer.data)


