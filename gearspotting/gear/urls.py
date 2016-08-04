from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from gearspotting.gear.models import Gear
from gearspotting.gear.views import (
    GearTagView, IndexView, TagsView, AddLinkView,
    AddPhotoView, EditLinksView, EditPhotosView)

info_dict = {
    'queryset': Gear.objects.all(),
}

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^create/?$', CreateView.as_view(model=Gear)),
    url(r'^tag/(?P<tag>[^/]+)/$', GearTagView.as_view(),
        name='gear_tag_detail'),
    url(r'^tag/$', TagsView.as_view()),
    url(r'^(?P<slug>[^/]+)/update/?$', UpdateView.as_view(model=Gear)),
    url(r'^(?P<slug>[^/]+)/delete/?$', DeleteView.as_view(model=Gear)),
    url(r'^(?P<slug>[^/]+)/$', DetailView.as_view(slug_field='slug',
                                                  model=Gear)),
    url(r'^(?P<slug>[^/]+)/edit_links/?$', EditLinksView.as_view()),
    url(r'^(?P<slug>[^/]+)/edit_photos/?$', EditPhotosView.as_view()),
    url(r'^(?P<slug>[^/]+)/add_link/$', AddLinkView.as_view()),
    url(r'^(?P<slug>[^/]+)/add_photo/$', AddPhotoView.as_view()),
]
