from django.urls import path
from .views import BlogPostView, BlogPostArrayView, UsersView, UserView, UserPostsView, AuthorPostsView, \
    BlogPostListView
from .api_views import BlogPostNewViewset

app_name = "posts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('posts/', BlogPostArrayView.as_view()),
    path('posts/<int:pk>', BlogPostView.as_view()),
    path('users/', UsersView.as_view()),
    path('users/<name>', UserView.as_view()),
    path('userposts/<name>', UserPostsView.as_view()),
    path('authorposts/<name>', AuthorPostsView.as_view()),
    path('blogpostlist/<username>', BlogPostListView.as_view()),
    path('blogpostview/', BlogPostNewViewset.as_view({'get': 'list'})),
]
