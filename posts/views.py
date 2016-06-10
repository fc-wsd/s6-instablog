from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Comment, Category

def list(request):
    lists = Post.objects.all().order_by('-pk')
    result = ''

    if lists.exists():
        for val in lists:
            result += '<hr><p>[{}] <a href="./{}">{}</a> / {} / {}</p><p>{}</p><hr>'\
                .format(val.category_rel.get(), val.pk, val.title, val.name, val.regdate.strftime('%Y-%m-%d %H:%M'), val.content)
    else:
        result = '<hr>Empty List<hr>'

    return HttpResponse(result)

def detail(request, post_id):
    val = Post.objects.filter(post_id=post_id).get()
    result = '<hr><p>[{}] {} {}</p><p>{}</p>'\
        .format(val.category_rel.get(), val.title, val.regdate.strftime('%Y-%m-d %H:%M'), val.content)

    comments = Comment.objects.filter(post_fk=val.pk)
    if comments.exists():
        for val in comments:
            result += '<hr>{}: {} - {}<hr>'.format(val.name, val.memo, val.regdate.strftime('%Y-%m-%d %H:%M'))
    else:
        result += '<hr>Empty Comment<hr>'

    return HttpResponse(result)