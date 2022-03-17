from django.urls import path
from rest_framework import routers
from api.views import CommentViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
#router.register(r'posts/{pk}', PostViewSet, basename='post-detail')
urlpatterns = router.urls
