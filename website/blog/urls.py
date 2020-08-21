from django.urls import path
from . import views

urlpatterns = [
    path('blogger/<str:pk>', views.bloggerPage, name='blogger'),
    path('', views.homePage, name='home'),
    path('post/<str:pk>', views.postPage, name='post'),
]
