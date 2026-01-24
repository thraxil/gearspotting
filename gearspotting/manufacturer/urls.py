from django.urls import path, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm
from gearspotting.manufacturer.views import (
    AddGearView,
    AddLinkView,
    EditLinksView,
)

app_name = "manufacturer"
urlpatterns = [
    path("", ListView.as_view(model=Manufacturer), name="manufacturer_index"),
    path(
        "create/",
        CreateView.as_view(model=Manufacturer, form_class=ManufacturerForm),
        name="manufacturer_create",
    ),
    path(
        "<slug:slug>/update/",
        UpdateView.as_view(model=Manufacturer, form_class=ManufacturerForm),
        name="manufacturer_update",
    ),
    path(
        "<slug:slug>/delete/",
        DeleteView.as_view(
            model=Manufacturer,
            success_url=reverse_lazy("manufacturer:manufacturer_index"),
        ),
        name="manufacturer_delete",
    ),
    path(
        "<slug:slug>/edit_links/",
        EditLinksView.as_view(),
        name="manufacturer_edit_links",
    ),
    path(
        "<slug:slug>/add_gear/",
        AddGearView.as_view(),
        name="manufacturer_add_gear",
    ),
    path(
        "<slug:slug>/",
        DetailView.as_view(model=Manufacturer),
        name="manufacturer_detail",
    ),
    path(
        "<slug:slug>/add_link/",
        AddLinkView.as_view(),
        name="manufacturer_add_link",
    ),
]
