from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer


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
