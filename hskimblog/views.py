from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.core.urlresolvers import reverse

from .models import *


def listing(request):
    page = request.GET.get('page', 1)
    category = int(request.GET.get('category', 1))
    per_page = 3

    # Post 및 Comment 갯수까지 구해온다.
    posts = Post.objects.filter(fk_category_id=category).order_by('-regdate').annotate(comment_count=Count('comment'))
    paginator = Paginator(posts, per_page)

    try:
        listing = paginator.page(page)
    except EmptyPage:
        listing = []
    except PageNotAnInteger:
        listing = paginator.page(1)

    context = {
        'categorys': Category.objects.all(),
        'listing': listing,
        'params' : {
            'page':page,
            'category':category,
        },
    }

    return render(request, 'listing.html', context)

def write(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        category = int(request.GET.get('category', 1))

        context = {
            'categorys': Category.objects.all(),
            'params' : {
                'page':page,
                'category':category,
            },
        }

        return render(request, 'write.html', context)
    elif request.method == 'POST':
        category = request.POST.get('category')
        writer = request.POST.get('writer')
        passwd = request.POST.get('passwd')
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post()
        post.writer = writer
        post.passwd = passwd
        post.title = title
        post.content = content
        post.save()

        # 카테고리 지정
        post.fk_category_id.add(Category.objects.get(pk=category))

        url = reverse('blog:detail', kwargs={'pk': post.pk})
        return redirect(url +"?category="+ category)

def detail(request, pk):
    page = request.GET.get('page', 1)
    category = int(request.GET.get('category', 1))

    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(fk_post_id=pk).order_by('-regdate')

    context = {
        'categorys': Category.objects.all(),
        'post': post,
        'comments': comments,
        'params' : {
            'page':page,
            'category':category,
        },
    }

    return render(request, 'detail.html', context)

def edit(request, pk):
    # 수정할 post 없는 경우 404 처리
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        page = request.GET.get('page', 1)
        category = int(request.GET.get('category', 1))

        context = {
            'categorys': Category.objects.all(),
            'post': post,
            'params': {
                'page': page,
                'category': category,
            },
        }

        return render(request, 'edit.html', context)
    elif request.method == 'POST':
        page = request.POST.get('page', 1)
        category = request.POST.get('category', 1)

        passwd = request.POST.get('passwd')
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 암호 불일치 시 404처리
        if post.passwd != passwd:
            raise Http404("암호가 일치하지 않습니다.")

        post.title = title
        post.content = content
        post.save()

        url = reverse('blog:detail', kwargs={'pk': post.pk})
        return redirect(url +"?page="+ page +"&category="+ category)

def delete(request, pk):
    page = request.GET.get('page', 1)
    category = int(request.GET.get('category', 1))

    # 수정할 post 없는 경우 404 처리
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        context = {
            'categorys': Category.objects.all(),
            'params': {
                'page': page,
                'category': category,
            },
        }

        return render(request, 'passwd.html', context)
    elif request.method == 'POST':
        page = request.POST.get('page', 1)
        category = request.POST.get('category', 1)

        passwd = request.POST.get('passwd')

        # 암호 불일치 시 404처리
        if post.passwd != passwd:
            raise Http404("암호가 일치하지 않습니다.")

        post.delete()

        url = reverse('blog:listing')
        return redirect(url +"?page="+ page +"&category="+ category)

def comment(request, post_id):
    # GET 요청 시 404 처리
    if request.method == 'GET':
        raise Http404("올바르지 않은 접근 입니다.")

    page = request.POST.get('page', 1)
    category = request.POST.get('category', 1)

    writer = request.POST.get('writer')
    passwd = request.POST.get('passwd')
    memo = request.POST.get('memo')

    post = get_object_or_404(Post, pk=post_id)

    comment = Comment()
    comment.writer = writer
    comment.passwd = passwd
    comment.memo = memo
    comment.fk_post_id = post
    comment.save()

    url = reverse('blog:detail', kwargs={'pk': post_id})
    return redirect(url +"?page="+ page +"&category="+ category)

def comment_del(request, post_id, pk):
    page = request.GET.get('page', 1)
    category = int(request.GET.get('category', 1))

    # 삭제할 comment 없는 경우 404 처리
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'GET':
        context = {
            'categorys': Category.objects.all(),
            'params': {
                'page': page,
                'category': category,
            },
        }

        return render(request, 'passwd.html', context)
    elif request.method == 'POST':
        page = request.POST.get('page', 1)
        category = request.POST.get('category', 1)

        passwd = request.POST.get('passwd')

        # 암호 불일치 시 404처리
        if comment.passwd != passwd:
            raise Http404("암호가 일치하지 않습니다.")

        comment.delete()

        url = reverse('blog:detail', kwargs={'pk': post_id})
        return redirect(url +"?page="+ page +"&category="+ category)