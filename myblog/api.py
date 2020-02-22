from rest_framework import routers
from blog import api_views as myapp_views

router = routers.DefaultRouter()
router.register('posts', myapp_views.BlogPostNewViewset)
router.register('users', myapp_views.UserViewset)

