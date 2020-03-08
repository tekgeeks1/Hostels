from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^hostel/', include('hostels.urls')),
     url(r'^accounts/', include('django.contrib.auth.urls')),
     url(r'^signup/$',  views.signup),
     url(r'^$', views.index , name='index'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
