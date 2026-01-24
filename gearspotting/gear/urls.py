from django.urls import path, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from gearspotting.gear.models import Gear
from gearspotting.gear.views import (
    AddLinkView,
    AddPhotoView,
    EditLinksView,
    EditPhotosView,
    GearDetailView,
    GearTagView,
    IndexView,
    TagsView,
)

app_name = "gear"
info_dict = {
    "queryset": Gear.objects.all(),
}

urlpatterns = [
    path("", IndexView.as_view(), name="gear_index"),
    path(
        "create/",
        CreateView.as_view(
            model=Gear, fields=["name", "manufacturer", "description"]
        ),
        name="gear_create",
    ),
    path("tag/<str:tag>/", GearTagView.as_view(), name="gear_tag_detail"),
    path("tag/", TagsView.as_view(), name="gear_tags"),
    path(
        "<slug:slug>/update/",
        UpdateView.as_view(
            model=Gear, fields=["name", "manufacturer", "description"]
        ),
        name="gear_update",
    ),
    path(
        "<slug:slug>/delete/",
        DeleteView.as_view(
            model=Gear, success_url=reverse_lazy("gear:gear_index")
        ),
        name="gear_delete",
    ),
    path("<slug:slug>/", GearDetailView.as_view(), name="gear_detail"),
    path(
        "<slug:slug>/edit_links/",
        EditLinksView.as_view(),
        name="gear_edit_links",
    ),
    path(
        "<slug:slug>/edit_photos/",
        EditPhotosView.as_view(),
        name="gear_edit_photos",
    ),
    path("<slug:slug>/add_link/", AddLinkView.as_view(), name="gear_add_link"),
    path(
        "<slug:slug>/add_photo/", AddPhotoView.as_view(), name="gear_add_photo"
    ),
]
