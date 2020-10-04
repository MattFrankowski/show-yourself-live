from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100, blank=True, null=True, default="Blogger hasn't set the Bio yet.")
    email = models.EmailField()
    photo = models.ImageField(upload_to="profile_pics", default="profile_pics/unnamed.png", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blogger/post/{self.id}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=350, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

