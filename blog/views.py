import logging

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required


from .models import Post
from .models import Category
from .models import Comment

from .forms import PostNormalForm
from .forms import PostForm

from instablog.sample_exceptions import HelloWorldError

logger = logging.getLogger('django')


def list_posts(request):
    logger.warning('경고 !!!')

    # raise HelloWorldError('뭔가 문제가 있다') # 내가 발생시킨 에러 발생 !
    # exc = HelloWorldError('?')
    # ecx.data = {'name': 'GB', 'content': 'not EU, }

    per_page = 2
    page = request.GET.get('page', 1)
    posts = Post.objects.all()

    pg = Paginator(posts, per_page)

    try:
        contents = pg.page(page)
    except PageNotAnInteger:
        contents = pg.page(1)
    except EmptyPage:
        contents = []

    ctx = {
        'posts': contents,
    }

    return render(request, 'list.html', ctx)


def detail_post(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)

        ctx = {
            'post': post,
        }
        return render(request, 'detail.html', ctx)
    elif request.method == 'POST':
        post = Post.objects.get(pk=pk)
        content = request.POST.get('content')

        new_comment = Comment()
        new_comment.post = post
        new_comment.content = content
        new_comment.save()

        url = reverse('blog:detail', kwargs={'pk': pk})
        return redirect(url)

# 모든 페이지에 로그인이 요구된다면 미들웨어를 사용하는것이 낫다
@login_required
def create_post(request):
    # 인증기능구현
    if not request.user.is_authenticated():
        raise Exception('누구세요??')

    form = PostForm()
    ctx = {
        'form': form,
    }
    if request.method == 'GET':
        return render(request, 'edit.html', ctx)
    elif request.method == 'POST':
        form = PostForm(request.POST)

        # title = request.POST.get('title')
        # content = request.POST.get('content')

        if form.is_valid() is True:
            new_post = form.save(commit=False) # False로 해두면 DB에 반영하지는 않지만 생성된 인스턴스 객체는 반환된다
            new_post.user = request.user # 유저 정보를 가진다
            new_post.save()
            # new_post = Post()
            # new_post.title = form.cleaned_data['title']
            # new_post.content = form.cleaned_data['content']
            # new_post.save()

            url = reverse('blog:detail', kwargs={'pk': new_post.pk})
            return redirect(url)

    else:
        form = PostForm()

    ctx = {'form': form, }

    return render(request, 'edit.html', ctx)


def modify_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        categories = Category.objects.all()
    else:
        form = request.POST
        category = get_object_or_404(Category, pk=form['category'])
        post.title = form['title']
        post.content = form['content']
        post.save()
        url = reverse('blog:detail', kwargs={'pk': post.pk})
        return redirect(url)

    return render(request, 'modify.html', {
        'post': post,
        'categories': categories,
    })


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')

    return render(request, 'delete.html', {
        'post': post,
    })
