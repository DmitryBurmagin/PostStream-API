from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts',
                PostViewSet,
                basename='posts'
                )
router.register(r'groups',
                GroupViewSet,
                basename='groups'
                )
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments'
                )
router.register(r'follow',
                FollowViewSet,
                basename='follow'
                )

urlpatterns = [
    path('v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
