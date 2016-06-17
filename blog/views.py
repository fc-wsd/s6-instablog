from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse


from .models import Post
from .models import Category
from .models import Comment


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
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)

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
