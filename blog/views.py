from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import Post


def list_posts(request):
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
    post = Post.objects.get(pk=pk)

    ctx = {
        'post': post,
    }
    return render(request, 'detail.html', ctx)
