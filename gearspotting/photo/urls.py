from django.conf.urls import url
from django.views.generic.detail import DetailView

from gearspotting.photo.models import Photo
from gearspotting.photo.views import ImportPhotoView

info_dict = {
    "queryset": Photo.objects.all(),
}

urlpatterns = [
    url(r"^(?P<pk>\d+)/$", DetailView.as_view(model=Photo)),
    url(r"^import/$", ImportPhotoView.as_view()),
]
