from django.urls import path, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.musiciangear.models import MusicianGear
from gearspotting.musiciangear.views import (
    AddLinkView,
    AddPhotoView,
    EditLinksView,
    EditPhotosView,
)

app_name = "musiciangear"
urlpatterns = [
    path("", ListView.as_view(model=MusicianGear), name="musiciangear_index"),
    path(
        "create/",
        CreateView.as_view(
            model=MusicianGear, fields=["musician", "gear", "description"]
        ),
        name="musiciangear_create",
    ),
    path(
        "<int:pk>/update/",
        UpdateView.as_view(
            model=MusicianGear, fields=["musician", "gear", "description"]
        ),
        name="musiciangear_update",
    ),
    path(
        "<int:pk>/delete/",
        DeleteView.as_view(
            model=MusicianGear,
            success_url=reverse_lazy("musiciangear:musiciangear_index"),
        ),
        name="musiciangear_delete",
    ),
    path(
        "<int:pk>/",
        DetailView.as_view(model=MusicianGear),
        name="musiciangear_detail",
    ),
    path(
        "<int:pk>/edit_links/",
        EditLinksView.as_view(),
        name="musiciangear_edit_links",
    ),
    path(
        "<int:pk>/edit_photos/",
        EditPhotosView.as_view(),
        name="musiciangear_edit_photos",
    ),
    path(
        "<int:pk>/add_link/",
        AddLinkView.as_view(),
        name="musiciangear_add_link",
    ),
    path(
        "<int:pk>/add_photo/",
        AddPhotoView.as_view(),
        name="musiciangear_add_photo",
    ),
]
