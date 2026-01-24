from django.urls import path, re_path
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

info_dict = {
    "queryset": Gear.objects.all(),
}

urlpatterns = [
    re_path(r"^$", IndexView.as_view(), name="gear_index"),
    path(
        "create/",
        CreateView.as_view(
            model=Gear, fields=["name", "manufacturer", "description"]
        ),
        name="gear_create",
    ),
    re_path(
        r"^tag/(?P<tag>[^/]+)/$", GearTagView.as_view(), name="gear_tag_detail"
    ),
    re_path(r"^tag/$", TagsView.as_view(), name="gear_tags"),
    path(
        "<slug:slug>/update/",
        UpdateView.as_view(
            model=Gear, fields=["name", "manufacturer", "description"]
        ),
        name="gear_update",
    ),
    path(
        "<slug:slug>/delete/",
        DeleteView.as_view(model=Gear, success_url="/gear/"),
        name="gear_delete",
    ),
    re_path(r"^(?P<slug>[^/]+)/$", GearDetailView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/edit_links/?$", EditLinksView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/edit_photos/?$", EditPhotosView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/add_link/$", AddLinkView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/add_photo/$", AddPhotoView.as_view()),
]
