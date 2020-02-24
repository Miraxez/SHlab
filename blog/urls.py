from django.urls import path

from .views import UserProfileView, UserPostsView

app_name = "posts"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/<int:user_id>/posts/', UserPostsView.as_view()),
    path('userprofile/<name>', UserProfileView.as_view()),
]
