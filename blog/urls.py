from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail_post, name='detail'),
    # pk라는 이름을 직접 명시 해준다. views.py의 method parameter의 순서들을 바꿀 수 있다.
    # 이렇게 할 때 list.html에서 <a href>를 사용할 때 pk로 명시해준다.
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail_post, name='detail'),
    url(r'^post/create/$', views.create_post, name='create'),
    url(r'^$', views.list_posts, name='list'),
]