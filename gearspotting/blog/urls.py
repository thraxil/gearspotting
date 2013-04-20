from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'gearspotting.blog.views',
    url(r'^$', 'index'),
    url(r'^post/$', 'add_post'),
    url((r'(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/'
         r'(?P<username>\w+)/(?P<slug>[\w\-]+)/$'),
        'post'),
)
