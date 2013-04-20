from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'gearspotting.blog.views',
    url(r'^$', 'index'),
)
