from django.urls import path
from django.views.generic.detail import DetailView

from gearspotting.photo.models import Photo
from gearspotting.photo.views import ImportPhotoView

app_name = "photo"
photo_qs = Photo.objects.all().prefetch_related(
    "gearphoto_set__gear__manufacturer",
    "musicianphoto_set__musician",
    "musiciangearphoto_set__musiciangear__musician",
    "musiciangearphoto_set__musiciangear__gear__manufacturer",
)

urlpatterns = [
    path(
        "<int:pk>/",
        DetailView.as_view(queryset=photo_qs),
        name="photo_detail",
    ),
    path("import/", ImportPhotoView.as_view(), name="photo_import"),
]
