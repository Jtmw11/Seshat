from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from Curator import views
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Seshat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^base/', include('Seshat.urls')), This line causes infinite recursion
    url(r'^document/', views.document, name='document'),
    url(r'^$', views.document)
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)