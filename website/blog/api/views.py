from rest_framework import generics

from .serializers import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    """
    Access a list of all blog posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a blog post.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer