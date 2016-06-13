from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse


from .models import Post
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
    post = Post.objects.get(pk=pk)
    comments=post.comment_set.all()
    ctx = {
        'post': post,
        'comments' : comments
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

def create_comment(request,pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        content = request.POST.get('content')

        new_comment = Comment()
        new_comment.post = post
        new_comment.content = content
        new_comment.save()

        url = reverse('blog:detail', kwargs={'pk': post.pk})
        return redirect(url)

def delete_comment(request,post_pk,commet_pk):
