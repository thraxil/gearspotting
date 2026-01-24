from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.musician.models import Musician, MusicianForm
from gearspotting.musician.views import (
    AddGearView,
    AddLinkView,
    AddPhotoView,
    EditGearView,
    EditLinksView,
    EditPhotosView,
    MusicianDetailView,
    MusicianTagView,
    TagsView,
)

app_name = "musician"
urlpatterns = [
    path("", ListView.as_view(model=Musician), name="musician_index"),
    path(
        "create/",
        CreateView.as_view(form_class=MusicianForm, model=Musician),
        name="musician_create",
    ),
    path(
        "<slug:slug>/update/",
        UpdateView.as_view(form_class=MusicianForm, model=Musician),
        name="musician_update",
    ),
    path(
        "<slug:slug>/delete/",
        DeleteView.as_view(
            model=Musician, success_url=reverse_lazy("musician:musician_index")
        ),
        name="musician_delete",
    ),
    path(
        "tag/<str:tag>/",
        MusicianTagView.as_view(),
        name="musician_tag_detail",
    ),
    path("tag/", TagsView.as_view(), name="musician_tags"),
    path(
        "<slug:slug>/add_link/",
        AddLinkView.as_view(),
        name="musician_add_link",
    ),
    path(
        "<slug:slug>/add_photo/",
        AddPhotoView.as_view(),
        name="musician_add_photo",
    ),
    path(
        "<slug:slug>/add_gear/",
        AddGearView.as_view(),
        name="musician_add_gear",
    ),
    path(
        "<slug:slug>/edit_links/",
        EditLinksView.as_view(),
        name="musician_edit_links",
    ),
    path(
        "<slug:slug>/edit_photos/",
        EditPhotosView.as_view(),
        name="musician_edit_photos",
    ),
    path(
        "<slug:slug>/edit_gear/",
        EditGearView.as_view(),
        name="musician_edit_gear",
    ),
    path("<slug:slug>/", MusicianDetailView.as_view(), name="musician_detail"),
]
