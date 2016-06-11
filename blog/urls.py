from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^post/([0-9]+)/$', views.detail_post),
    url(r'^$', views.list_posts),
]