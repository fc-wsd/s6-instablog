# blog/urls.py

from django.conf.urls import url

from . import views


app_name = 'blog'

urlpatterns = [
    url(r'^comment/delete/(?P<pk>[0-9]+)/$',views.delete_comment, name ="delete_comment"),
    url(r'^comment/create/(?P<pk>[0-9]+)/$',views.create_comment, name ="create_comment"),
    url(r'^posts/create/$', views.create_post, name='create_post'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.detail_post, name='detail'),
    url(r'^$', views.list_posts, name='list'),
]
