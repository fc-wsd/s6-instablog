from django.conf.urls import url

from .views import *

app_name = 'blog'

urlpatterns = [
    url(r'^comment/del/(?P<post_id>[0-9]+)/(?P<pk>[0-9]+)/$', comment_del, name='comment_del'),
    url(r'^comment/(?P<post_id>[0-9]+)/$', comment, name='comment'),
    url(r'^delete/(?P<pk>[0-9]+)/$', delete, name='delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', edit, name='edit'),
    url(r'^write/$', write, name='write'),
    url(r'^detail/(?P<pk>[0-9]+)/$', detail, name='detail'),
    url(r'^$', listing, name='listing'),
]