from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm
from .forms import PostNormalForm
from instablog.sample_exceptions import HelloWorldError


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
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)

    ctx = {
        'post': post,
    }
    return render(request, 'detail.html', ctx)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)

        if form.is_valid() is True:
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()

            url = reverse('blog:detail', kwargs={'pk': new_post.pk})
            return redirect(url)
    else:
        form = PostForm()

    ctx = {'form': form, }

    return render(request, 'edit.html', ctx)




