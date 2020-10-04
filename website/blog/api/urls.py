from django.urls import path
from .views import PostDetail, PostList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('post/<str:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post_list/', PostList.as_view(), name='post-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)