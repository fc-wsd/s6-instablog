from django.test import TestCase
from django.test import Client
from django.db import transaction
from django.db.utils import IntegrityError
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Post

class PostTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(
            username = 'test', password='1234'
        )

    def test_import_post_model(self):
        Post = None
        try:
            from blog.models import Post
        except ImportError:
            pass

        self.assertIsNotNone(Post)

    def test_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장하는 테스트.
        검증 방법 : 저장한 뒤 모델 매니저로 저장한 데이터를 가져와서 비교
        '''
        u1 = User.objects.first()

        new_post = Post()
        new_post.user = u1
        new_post.title = 'test'
        new_post.content = '1234'
        new_post.save()

        self.assertIsNotNone(new_post.pk)
        exists = Post.objects.filter(pk=new_post.pk).exists()
        self.assertTrue(exists)

    def test_failed_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장할 때 실패하는 경우에 대한 테스트
        '''
        new_post = Post()
        new_post.title = 'test'
        new_post.content = '1234'

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_post.save()

    def test_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보는 url로 접근하는 테스트
        '''
        u1 = User.objects.first()

        new_post = Post()
        new_post.user = u1
        new_post.title = 'test'
        new_post.content = '1234'
        new_post.save()

        client = Client()
        url = reverse('blog:detail', kwargs={'pk':new_post.pk})
        result = client.get(url)

        self.assertEqual(result.status_code, 200)

    def test_failed_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보지 못하고
        실패하는 경우에 대한 테스트
        '''
        client = Client()
        url = reverse('blog:detail', kwargs={'pk':1})
        result = client.get(url)

        self.assertEqual(result.status_code, 404)