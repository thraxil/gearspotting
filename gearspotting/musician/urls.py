from django.conf.urls.defaults import patterns, url

from gearspotting.musician.models import Musician, MusicianForm
from tagging.views import tagged_object_list

info_dict = {
    'queryset': Musician.objects.all(),
}

urlpatterns = patterns(
    '',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^create/?$', 'django.views.generic.create_update.create_object',
     dict(form_class=MusicianForm, post_save_redirect="/musician/")),
    (r'^(?P<slug>[^/]+)/update/?$',
     'django.views.generic.create_update.update_object',
     dict(form_class=MusicianForm, post_save_redirect="/musician/")),
    (r'^(?P<slug>[^/]+)/delete/?$',
     'django.views.generic.create_update.delete_object',
     dict(model=Musician, post_delete_redirect="/musician/")),
    url(r'^tag/(?P<tag>[^/]+)/$',
        tagged_object_list,
        dict(queryset_or_model=Musician, paginate_by=100, allow_empty=True,
             template_name="musician/musician_tag_list.html"),
        name='musician_tag_detail'),
    url(r'^tag/$', 'gearspotting.musician.views.tags'),
    (r'^(?P<slug>[^/]+)/edit_links/?$',
     'gearspotting.musician.views.edit_links'),
    (r'^(?P<slug>[^/]+)/add_link/$', 'gearspotting.musician.views.add_link'),
    (r'^(?P<slug>[^/]+)/add_photo/$', 'gearspotting.musician.views.add_photo'),
    (r'^(?P<slug>[^/]+)/add_gear/$', 'gearspotting.musician.views.add_gear'),
    (r'^(?P<slug>[^/]+)/edit_photos/?$',
     'gearspotting.musician.views.edit_photos'),
    (r'^(?P<slug>[^/]+)/edit_gear/?$',
     'gearspotting.musician.views.edit_gear'),
    (r'^(?P<slug>[^/]+)/$',
     'django.views.generic.list_detail.object_detail',
     info_dict),
)
