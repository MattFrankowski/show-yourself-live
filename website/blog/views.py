from django.shortcuts import render
from .models import Blogger, Post


def homePage(request):
    context = {

    }
    return render(request, 'blog/home.html', context)


def bloggerPage(request, pk):
    blogger = Blogger.objects.get(id=pk)
    posts = blogger.post_set.all()[:5]
    context = {
        'blogger': blogger,
        'posts': posts,
    }
    return render(request, 'blog/blogger.html', context)


def postPage(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)