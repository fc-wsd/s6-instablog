from django.conf.urls import url
from django.contrib import admin

from blog.views import list_posts


urlpatterns = [
    url(r'^hello/$', list_posts),
    url(r'^admin/', admin.site.urls),
]
