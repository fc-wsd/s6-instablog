from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^login/$', login, name='login_url'),
    url(r'^logout/$', logout, name='logout_url'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]
