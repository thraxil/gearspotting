from django.conf.urls.defaults import *

urlpatterns = patterns('gear.views',
                       (r'^$', 'index'),
                       (r'^add_manufacturer','add_manufacturer'),
#                       (r'^create/?$', 'views.create'),
#                       (r'^tag/(?P<tag>[^/]+)/$','views.gear_tag'),
#                       (r'^tag/$','views.tags'),
)
