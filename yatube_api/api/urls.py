from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts',
                   PostViewSet,
                   basename='posts'
                   )
router_v1.register('groups',
                   GroupViewSet,
                   basename='groups'
                   )
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments'
                   )
router_v1.register('follow',
                   FollowViewSet,
                   basename='follow'
                   )

v1_patterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
