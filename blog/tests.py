from django.test import TestCase
from django.test import Client
from django.db import transaction
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
from django.core.exceptions import ObjectDoesNotExist

from .models import Post

User = get_user_model()
'''
class PostTest(TestCase):

    def setUp(self):
        self.u1 = User.objects.create_user(
        username = 'hello', password='helloworld'
        )
    def test_add(self):
        self.assertTrue(1 == 1)

    def test_failed_create_post(self):
        new_post = Post()
        new_post.title ='hello'
        new_post.content = 'world'

        with transaction.atomic():
            with self.assertRaises(IntegrityError):
                new_post.save()

    def test_create_post(self):
        u1 = User.objects.first()

        new_post = Post()
        new_post.user = u1
        new_post.title ='hello'
        new_post.content = 'world'
        new_post.save()


        self.assertIsNotNone(new_post.pk)

        exists = Post.objects.filter(pk=new_post.pk).exists()
        self.assertTrue(exists)

    def test_client_detail_post(self):
        c = Client()

        p = Post()
        p.user = self.u1
        p.title = 'qqqqq'
        p.content = 'zzzzz'
        p.save()

        url = reverse('blog:detail', kwargs = {'pk':p.pk})
        res = c.get(url)
        self.assertEqual(res.status_code,200)
'''
class PhotoModelTest(TestCase):
    def test_import_post_model(self):
        Post = None
        try:
            from blog.models import Post
        except ImportError:
            pass

        self.assertIsNotNone(Post)
    def setUp(self):
        self.u1 = User.objects.create_user(
            username = 'namshook', password='helloworld'
        )

    def test_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장하는 테스트.
        검증 방법 : 저장한 뒤 모델 매니저로 저장한 데이터를 가져와서 비교
        '''

        d_post = Post()
        d_post.user = self.u1
        d_post.title = 'hello'
        d_post.content = 'world'
        d_post.save()

        g_post = Post.objects.get(user = self.u1)

        self.assertEqual(d_post, g_post)


    def test_failed_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장할 때 실패하는 경우에 대한 테스트
        '''
        d_post = Post()
        d_post.title = 'hello'
        d_post.content = 'world'


        with self.assertRaises(IntegrityError) as cm:
            d_post.save()

        


    def test_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보는 url로 접근하는 테스트
        '''
        d_client = Client()
        d_post = Post()
        d_post.user = self.u1
        d_post.title = 'ohio'
        d_post.content = '좋은아침'
        d_post.save()


        url = reverse('blog:detail', kwargs = {'pk': d_post.pk})
        res = d_client.get(url)
        self.assertEqual(res.status_code,200)



    def test_failed_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보지 못하고
        실패하는 경우에 대한 테스트
        '''
        d_client = Client()
        d_post = Post()
        d_post.user = self.u1
        d_post.title = 'ohio'
        d_post.content = '좋은아침'
        d_post.save()





        url = reverse('blog:detail', kwargs = {'pk': 100})

        with self.assertRaises(ObjectDoesNotExist) as cm:
            res = d_client.get(url)
