from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^login/$', login,
        name='login_url',
        kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', logout,
        name='logout_url',
        kwargs={'next_page': '/login/'}),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)