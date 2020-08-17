from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views

from . import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_views.obtain_auth_token),
]
