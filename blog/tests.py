from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse, Resolver404
from django.db import transaction
from django.http import Http404
from django.test import TestCase, Client


class PhotoModelTest(TestCase):
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
        from blog.models import Post
        post = Post()
        post.title = '테스트 제목'
        post.content = '테스트 컨텐츠'
        with transaction.atomic():
            post.save()

        saved_post = Post.objects.get(pk=post.pk);
        self.assertEqual(post, saved_post)



    def test_failed_save_post_by_model(self):
        '''Post 모델을 이용해 데이터를 저장할 때 실패하는 경우에 대한 테스트
        '''
        from blog.models import Category, Post
        post = Post()
        post.title = '테스트 제목2'
        post.content = '테스트 컨텐츠2'
        category = Category()
        post.category = category

        with transaction.atomic():
            with self.assertRaises(ValueError):
                post.save()


    def test_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보는 url로 접근하는 테스트
        '''
        from blog.models import Post
        post = Post()
        post.title = '테스트 제목3'
        post.content = '테스트 컨텐츠3'
        with transaction.atomic():
            post.save()

        c = Client()

        url = reverse('blog:detail', kwargs={'pk': post.pk})
        res = c.get(url)
        self.assertEqual(res.status_code, 200)


    def test_failed_get_post_by_url(self):
        '''Django Test Client를 이용해 특정 게시물을 보지 못하고
        실패하는 경우에 대한 테스트
        '''
        from blog.models import Post
        c = Client()

        url = reverse('blog:detail', kwargs={'pk': 0})

        with self.assertRaises(Post.DoesNotExist):
            c.get(url)

