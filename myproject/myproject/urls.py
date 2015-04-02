from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import posts

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name='index.html'), name="index"),
    #url(r'^$', posts.views.http_resp),
)
