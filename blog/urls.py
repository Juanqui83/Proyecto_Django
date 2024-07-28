from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, ProfileViewSet, CategoryAPIView, UserPostsAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryAPIView.as_view()),
    path('users/<str:username>/posts/', UserPostsAPIView.as_view()),
]
