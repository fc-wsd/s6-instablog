from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.list, name='list'),
    url('^(?P<post_id>[0-9]+)/$', views.detail, name='detail')
]