from django.shortcuts import render

from .models import Post

def list_posts(request):
    posts = Post.objects.all()
    ctx = {
        'object_list': posts,
    }
    return render(request, 'list.html', ctx)

def detail_post(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {
        'post': post,
    }
    return render(request, 'detail.html', ctx)