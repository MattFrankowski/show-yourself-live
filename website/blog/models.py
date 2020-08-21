from django.db import models


class Blogger(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    #phone_number = models.PhoneNumberField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    images = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
