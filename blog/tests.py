from django.test import TestCase
from django.test import Client
from django.db.utils import IntegrityError
from django.db import transaction
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import Post

User = get_user_model()


# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(
            username='hello', password='helloworld',
        )

    # 규칙 test_
    def test_add(self):
        self.assertTrue(1 == 1)

    def test_failed_create_post(self):
        new_post = Post()
        new_post.title = 'hello'
        new_post.content = 'world'
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_post.save() # 장고가 자동으로 만드는 test용 DB에 저장됨
                # transaction 처리가 필요하다

    def test_create_post(self):
        u1 = User.objects.first()
        new_post = Post()
        new_post.user = u1
        new_post.title = 'hello'
        new_post.content = 'world'
        new_post.save()

        self.assertIsNotNone(new_post.pk)

        # p1 = Post.objects.get(pk=new_post.pk)
        exists = Post.objects.filter(pk=new_post.pk).exists()
        self.assertTrue(exists)

    def test_client_detail_post(self):
        c = Client()
        p = Post()
        p.user = self.u1
        p.title = 'qqqq'
        p.content = 'zzzz'
        p.save()

        # url = '/blog/posts/{}/'.format(p.pk)
        # c.get(url)
        url = reverse('blog:detail', kwargs={'pk': p.pk})
        res = c.get(url)

        self.assertEqual(res.status_code, 200)


class PhotoModelTest(TestCase):
    def setUp(self):
        self.u2 = User.objects.create_user(
            username='jaemin', password='dlawoals',
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
        u2 = User.objects.first()
        new_post = Post()
        new_post.user = u2
        new_post.title = 'test'
        new_post.content = 'test'
        new_post.save()
        self.assertIsNotNone(new_post.pk)
        exists = Post.objects.filter(pk=new_post.pk).exists()
        self.assertTrue(exists)

    def test_failed_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장할 때 실패하는 경우에 대한 테스트
        '''
        new_post = Post()
        new_post.content = 'fail'
        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_post.save()


    def test_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보는 url로 접근하는 테스트
        '''
        c = Client()
        p = Post()
        p.user = self.u2
        p.title = 'test'
        p.content = 'test'
        p.save()
        url = reverse('blog:detail', kwargs={'pk': p.pk})
        res = c.get(url)
        self.assertEqual(res.status_code, 200)

    def test_failed_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보지 못하고
        실패하는 경우에 대한 테스트
        '''
        c = Client()
        url = reverse('blog:detail', kwargs={'pk': 100})
        res = c.get(url)
        self.assertEqual(res.status_code, 404)
