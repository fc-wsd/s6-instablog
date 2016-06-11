from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from .models import Post

def list_posts(request):
    # per_page = 2
    # try:
    #     page = int(request.GET.get('page', 1))
    #     page = page if page >= 1 else 1
    # except ValueError:
    #     # app_name 과 urls.py에 매칭 시킨 url의 이름
    #     return redirect('blog:list')
    #
    # posts = Post.objects.all()
    # posts = posts[(page-1)*per_page: page*per_page]

    per_page = 5
    page_number = request.GET.get('page', 1)

    posts = Post.objects.all()
    pg = Paginator(posts, per_page)
    try:
        contents = pg.page(page_number)
    except PageNotAnInteger:
        return redirect('blog:list')
    except EmptyPage:
        return redirect('blog:list')
    ctx = {
        'object_list': contents,
    }
    return render(request, 'list.html', ctx)

def detail_post(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {
        'post': post,
    }
    return render(request, 'detail.html', ctx)


def create_post(request):
    if request.method == 'GET':
        return render(request, 'edit.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        new_post = Post()
        new_post.title = title
        new_post.content = content
        new_post.category_id = 0
        new_post.save()

        url = reverse('blog:detail', kwargs={'pk': new_post.pk,})
        return redirect(url)
    else:
        return redirect('blog:list')