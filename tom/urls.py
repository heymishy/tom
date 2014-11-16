from django.conf.urls import patterns, include, url
from django.contrib import admin
from backend import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^backend/', include('backend.urls',)),
    url(r'^admin/', include(admin.site.urls)),
)