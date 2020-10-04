from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
import os
from datetime import datetime

from .models import Blogger, Post, Comment

class SigninTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class BloggerTestCase(TestCase):

    def setUp(self):
        self.blogger = Blogger.objects.create(user=get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com'),
                                              name="John Doe",
                                              bio="Test Bio",
                                              email="test@example.com",
                                              photo=os.path.join(settings.BASE_DIR, "static/profile_pics/unnamed.png"),
                                              date_created=datetime.now()
                                              )

    def tearDown(self):
        self.blogger.delete()

    def test_user(self):
        user = authenticate(username=self.blogger.user.username, password=self.blogger.user.password)
        self.assertFalse(user is not None and user.is_authenticated)

    def test_name(self):
        self.assertTrue(self.blogger.name == "John Doe")

    def test_bio(self):
        self.assertTrue(self.blogger.bio == "Test Bio")

    def test_email(self):
        self.assertTrue(self.blogger.email == "test@example.com")

    def test_photo(self):
        photo = self.blogger.photo
        self.assertTrue(photo is not None)

    def test_date(self):
        date_created = self.blogger.date_created
        self.assertTrue(isinstance(date_created, datetime))


class PostTestCase(TestCase):

    def setUp(self):
        self.post = Post.objects.create(title="Test title",
                                        content="Test content",
                                        image=os.path.join(settings.BASE_DIR, "static/post_images/shawn-ang-nmpW_WwwVSc-unsplash_G7cJZoJ.jpg"),
                                        author=Blogger.objects.create(
                                            user=get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com'),
                                            name="John Doe",
                                            bio="Test Bio",
                                            email="test@example.com",
                                            photo=os.path.join(settings.BASE_DIR, "static/profile_pics/unnamed.png"),
                                            date_created=datetime.now()
                                            ),
                                        date_created=datetime.now()
                                        )

    def tearDown(self):
        self.post.delete()

    def test_title(self):
        self.assertTrue(self.post.title == "Test title")

    def test_content(self):
        self.assertTrue(self.post.content == "Test content")

    def test_image(self):
        self.assertTrue(self.post.image is not None)

    def test_blogger(self):
        author = self.post.author
        self.assertTrue(author is not None and isinstance(author, Blogger))

    def test_date(self):
        date_created = self.post.date_created
        self.assertTrue(isinstance(date_created, datetime))


class CommentTestCase(TestCase):

    def setUp(self):
        self.comment = Comment.objects.create(
            user=get_user_model().objects.create_user(username='test1', password='12test12', email='test@example.com'),
            post=Post.objects.create(
                title="Test title",
                content="Test content",
                image=os.path.join(settings.BASE_DIR, "static/post_images/shawn-ang-nmpW_WwwVSc-unsplash_G7cJZoJ.jpg"),
                author=Blogger.objects.create(
                    user=get_user_model().objects.create_user(username='test2', password='12test12', email='test@example.com'),
                    name="John Doe",
                    bio="Test Bio",
                    email="test@example.com",
                    photo=os.path.join(settings.BASE_DIR, "static/profile_pics/unnamed.png"),
                    date_created=datetime.now()
                ),
            ),
            content="Comment text",
            date_created=datetime.now()
        )

    def tearDown(self):
        self.comment.delete()

    def test_user(self):
        self.assertTrue(self.comment.user is not None)

    def test_post(self):
        self.assertTrue(self.comment.post is not None)

    def test_content(self):
        self.assertTrue(self.comment.content == "Comment text")

    def test_date(self):
        date_created = self.comment.date_created
        self.assertTrue(isinstance(date_created, datetime))