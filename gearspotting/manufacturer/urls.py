from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from gearspotting.manufacturer.models import Manufacturer, ManufacturerForm
from gearspotting.manufacturer.views import (AddGearView, AddLinkView,
                                             EditLinksView)

urlpatterns = [
    url(r"^$", ListView.as_view(model=Manufacturer)),
    url(
        r"^create/?$",
        CreateView.as_view(model=Manufacturer, form_class=ManufacturerForm),
    ),
    url(
        r"^(?P<slug>[^/]+)/update/?$",
        UpdateView.as_view(model=Manufacturer, form_class=ManufacturerForm),
    ),
    url(r"^(?P<slug>[^/]+)/delete/?$", DeleteView.as_view(model=Manufacturer)),
    url(r"^(?P<slug>[^/]+)/edit_links/?$", EditLinksView.as_view()),
    url(r"^(?P<slug>[^/]+)/add_gear/$", AddGearView.as_view()),
    url(r"^(?P<slug>[^/]+)/$", DetailView.as_view(model=Manufacturer)),
    url(r"^(?P<slug>[^/]+)/add_link/$", AddLinkView.as_view()),
]
