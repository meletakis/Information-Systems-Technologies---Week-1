from django.conf.urls import patterns, include, url

from posts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^(?P<postid>\d+)', views.getpost,),
    url(r'^user/(?P<userid>\d+)', views.getuser, ),
)
