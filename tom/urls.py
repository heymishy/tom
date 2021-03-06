from django.conf.urls import patterns, include, url
from django.contrib import admin
from backend import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^backend/', include('backend.urls', namespace="backend")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),	

    # registration module urls
    #(r'^accounts/', include('registration.backends.simple.urls')),
)