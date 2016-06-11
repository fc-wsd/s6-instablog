from django.shortcuts import render
from django.shortcuts import redirect


from .models import Post


def list_posts(request):
    per_page = 2
    # if 'page' in request.GET:
    #     page = request.GET['page']
    # else:
    #     page = 1
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except ValueError:
        return redirect('blog:list')
        # page = 1

    page = page if page >= 1 else 1

    posts = Post.objects.all()
    posts = posts[(page-1)*per_page:page*per_page]


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





