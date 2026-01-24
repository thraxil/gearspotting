from django.urls import re_path
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm
from gearspotting.manufacturer.views import (
    AddGearView,
    AddLinkView,
    EditLinksView,
)

urlpatterns = [
    re_path(r"^$", ListView.as_view(model=Manufacturer)),
    re_path(
        r"^create/?$",
        CreateView.as_view(model=Manufacturer, form_class=ManufacturerForm),
    ),
    re_path(
        r"^(?P<slug>[^/]+)/update/?$",
        UpdateView.as_view(model=Manufacturer, form_class=ManufacturerForm),
    ),
    re_path(
        r"^(?P<slug>[^/]+)/delete/?$", DeleteView.as_view(model=Manufacturer, success_url="/manufacturer/")
    ),
    re_path(r"^(?P<slug>[^/]+)/edit_links/?$", EditLinksView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/add_gear/$", AddGearView.as_view()),
    re_path(r"^(?P<slug>[^/]+)/$", DetailView.as_view(model=Manufacturer)),
    re_path(r"^(?P<slug>[^/]+)/add_link/$", AddLinkView.as_view()),
]
