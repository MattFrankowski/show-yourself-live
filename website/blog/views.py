from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Blogger, Post
from .forms import PostForm, UserForm, BloggerForm, CommentForm
from .decorators import unauthenticated_user


class HomeListView(ListView):
    model = Blogger
    context_object_name = "bloggers"
    template_name = "blog/home.html"

    def get_queryset(self):
        return Blogger.objects.all().order_by("-date_created")[:3]


@login_required(login_url='/login/')
def bloggerView(request):
    """
    Blogger Page view. Get logged Blogger and retrieve Posts
    """
    blogger = request.user.blogger
    posts = blogger.post_set.all()
    paginator = Paginator(posts, 6)  # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogger': blogger,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blogger.html', context)


@login_required(login_url='/login/')
def postView(request, post_id):
    """
    Post Page view. Get certain Post object.
    """
    post = request.user.blogger.post_set.get(id=post_id)
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy("blogger")
    login_url = "/login"

    def get_initial(self, **kwargs):
        initial = super(PostCreateView, self).get_initial(**kwargs)
        initial["author"] = self.request.user.blogger
        return initial


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image"]
    template_name = "blog/update_post.html"
    login_url = "/login"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blogger")
    login_url = "/login"


@unauthenticated_user
def registerView(request):
    """
    Register User view. Uses UserForm
    """
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account created for " + username)
            return redirect('login')

    context = {
        'form': form,
    }
    # template stored in website/templates/registration directory
    return render(request, 'registration/register.html', context)


@login_required(login_url='/login/')
def userView(request):
    """
    View displays User information
    """
    context = {
        "user": request.user,
    }
    return render(request, 'blog/user.html', context)


@login_required(login_url='/login/')
def createBlogView(request):
    """
    Create Blog view. Uses BloggerForm
    """
    data = {
        'user': request.user,
        'email': request.user.email,
    }

    bloggerForm = BloggerForm(initial=data)

    if request.method == "POST":
        bloggerForm = BloggerForm(request.POST, request.FILES)
        if bloggerForm.is_valid():
            bloggerForm.save()
            return redirect("home")

    context = {
        "bloggerForm": bloggerForm,
    }

    return render(request, "blog/create_blog.html", context)


class AboutView(TemplateView):
    template_name = "blog/about.html"


def searchResultsView(request):
    """
    Perform a Blogger search based on a given name
    """
    bloggerName = request.GET.get("search_blogger")
    bloggers = Blogger.objects.all().filter(name__icontains=bloggerName)

    context = {
            "bloggers": bloggers,
        }
    return render(request, "blog/search_results.html", context)


def bloggerVisitView(request, pk):
    """
    Blogger Visit view. User cannot edit an object as a visitor.
    """
    blogger = Blogger.objects.get(id=pk)
    posts = blogger.post_set.all()
    paginator = Paginator(posts, 6)  # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogger": blogger,
        "posts": posts,
        "page_obj": page_obj,
    }
    return render(request, "blog/blogger_visit.html", context)


def postVisitView(request, pk, post_id):
    """
    Post Visit view. User cannot edit an object as a visitor.
    """
    post = Blogger.objects.get(id=pk).post_set.get(id=post_id)
    comments = post.comment_set.all().order_by("-date_created")

    data = {
        "user": request.user,
        "post": post,
    }

    form = CommentForm(initial=data)

    if request.method == "POST":
        form = CommentForm(request.POST, initial=data)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger/{pk}/post/{post_id}")

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/post_visit.html", context)
