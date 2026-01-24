from django.urls import path
from django.views.generic.detail import DetailView

from gearspotting.photo.models import Photo
from gearspotting.photo.views import ImportPhotoView

app_name = "photo"
info_dict = {
    "queryset": Photo.objects.all(),
}

urlpatterns = [
    path("<int:pk>/", DetailView.as_view(model=Photo), name="photo_detail"),
    path("import/", ImportPhotoView.as_view(), name="photo_import"),
]
