from django.conf.urls.defaults import patterns

from gearspotting.photo.models import Photo

info_dict = {
    'queryset': Photo.objects.all(),
}

urlpatterns = patterns(
    '',
    (r'^(?P<object_id>\d+)/$',
     'django.views.generic.list_detail.object_detail', info_dict),
    (r'^import/$', 'photo.views.import_photo'),
)
