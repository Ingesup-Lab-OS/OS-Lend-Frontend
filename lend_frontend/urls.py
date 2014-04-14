from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vmlocation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lend_frontend.views.index', name='index'),
    url(r'^flavor/(?P<id>[_a-zA-Z0-9\-]+)/$', 'lend_frontend.views.flavor', name='flavor'),
    url(r'^heat_template/(?P<id>\w+)/$', 'lend_frontend.views.heat_template', name='heat_template')
)