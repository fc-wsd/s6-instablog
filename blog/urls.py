# blog/urls.py

from django.conf.urls import url

from . import views


app_name = 'blog'

urlpatterns = [
    url(r'posts/(?P<pk>[0-9]+)/delete/$', views.delete_post, name='delete'),
    url(r'^posts/(?P<pk>[0-9]+)/modify/$', views.modify_post, name='modify'),
    url(r'^posts/create/$', views.create_post, name='create'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.detail_post, name='detail'),
    url(r'^$', views.list_posts, name='list'),
]

