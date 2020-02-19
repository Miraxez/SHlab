from django.urls import path
from .views import BlogPostView
app_name = "posts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('posts/', BlogPostView.as_view()),
    path('posts/<int:pk>', BlogPostView.as_view())
]