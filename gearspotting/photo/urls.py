from django.conf.urls.defaults import patterns
from django.views.generic.detail import DetailView

from gearspotting.photo.models import Photo
from gearspotting.photo.views import ImportPhotoView

info_dict = {
    'queryset': Photo.objects.all(),
}

urlpatterns = patterns(
    '',
    (r'^(?P<pk>\d+)/$', DetailView.as_view(model=Photo)),
    (r'^import/$', ImportPhotoView.as_view()),
)
