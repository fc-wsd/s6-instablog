from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
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


def create_post(request):
    ctx = {}
    if request.method == 'GET':
        return render(request, 'edit.html', ctx)
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        new_post = Post()
        new_post.title = title
        new_post.content = content
        new_post.save()

        url = reverse('blog:detail', kwargs={'pk': new_post.pk})
        return redirect(url)

    return render(request, 'edit.html', ctx)

