from django.urls import re_path
from django.views.generic.detail import DetailView

from gearspotting.photo.models import Photo
from gearspotting.photo.views import ImportPhotoView

info_dict = {
    "queryset": Photo.objects.all(),
}

urlpatterns = [
    re_path(r"^(?P<pk>\d+)/$", DetailView.as_view(model=Photo)),
    re_path(r"^import/$", ImportPhotoView.as_view()),
]
