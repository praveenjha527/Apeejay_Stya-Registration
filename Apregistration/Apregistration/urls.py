from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Apregistration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^grappelli/', include('grappelli.urls')), # Customised Django_admin Urls
    url(r'^admin/', include(admin.site.urls)),
)
