from django.conf.urls.defaults import patterns
from django.views.generic.detail import DetailView

from gearspotting.photo.models import Photo

info_dict = {
    'queryset': Photo.objects.all(),
}

urlpatterns = patterns(
    '',
    (r'^(?P<pk>\d+)/$', DetailView.as_view(model=Photo)),
    (r'^import/$', 'gearspotting.photo.views.import_photo'),
)
