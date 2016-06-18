from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model

from .models import Post


User = get_user_model()


class PostTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(
            username='hello', password='helloworld'
        )

    def test_add(self):
        self.assertTrue(1 == 1)

    def test_failed_create_post(self):
        new_post = Post()
        new_post.title = 'hello'
        new_post.content = 'world'

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_post.save()

    def test_create_post(self):
        u1 = User.objects.first()

        new_post = Post()
        new_post.user = u1
        new_post.title = 'hello'
        new_post.content = 'world'
        new_post.save()

        self.assertIsNotNone(new_post.pk)

        exists = Post.objects.filter(pk=new_post.pk).exists()
        self.assertTrue(exists)

