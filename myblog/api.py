from rest_framework import routers

from blog import views as myapp_views

router = routers.DefaultRouter()
router.register('posts', myapp_views.BlogPostViewset)
router.register('users', myapp_views.UserViewset)
