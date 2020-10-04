from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('blogger/', bloggerView, name='blogger'),

    path('blogger/post/<str:post_id>', postView, name='post'),
    path('blogger/create_post', PostCreateView.as_view(), name="create_post"),
    path('blogger/post/<str:pk>/update', PostUpdateView.as_view(), name='update_post'),
    path('blogger/post/<str:pk>/delete', PostDeleteView.as_view(), name='delete_post'),

    path('blogger/<str:pk>', bloggerVisitView, name='blogger_visit'),
    path('blogger/<str:pk>/post/<str:post_id>', postVisitView, name='post_visit'),


    path('about/', AboutView.as_view(), name='about'),

    path('register/', registerView, name='register'),

    path('user/', userView, name='user'),
    path('user/create_blog', createBlogView, name='create_blog'),


    path('search_results/', searchResultsView, name='search_results'),
]
