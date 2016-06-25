from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^logout/$', logout,name="logout_url",kwargs={'next_page': 'login.html'}),
    url(r'^login/$', login,
         name='login_url',
         kwargs={'template_name': 'login.html'}),

    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                    document_root = settings.MEDIA_ROOT)
#handler404 = 'blog.views.my_handler404'    뷰함수를 사용하고싶을때
