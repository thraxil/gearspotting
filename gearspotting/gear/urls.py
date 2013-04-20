from django.conf.urls.defaults import patterns, url

from gearspotting.gear.models import Gear
from tagging.views import tagged_object_list

info_dict = {
    'queryset': Gear.objects.all(),
}

urlpatterns = patterns(
    '',
    (r'^$', 'gearspotting.gear.views.index'),
    (r'^create/?$', 'django.views.generic.create_update.create_object',
     dict(model=Gear, post_save_redirect="/gear/")),
    url(r'^tag/(?P<tag>[^/]+)/$',
        tagged_object_list,
        dict(queryset_or_model=Gear, paginate_by=100, allow_empty=True,
             template_name="gear/gear_tag_list.html"),
        name='gear_tag_detail'),
    url(r'^tag/$', 'gearspotting.gear.views.tags'),
    (r'^(?P<slug>[^/]+)/update/?$',
     'django.views.generic.create_update.update_object',
     dict(model=Gear, post_save_redirect="/gear/")),
    (r'^(?P<slug>[^/]+)/delete/?$',
     'django.views.generic.create_update.delete_object',
     dict(model=Gear, post_delete_redirect="/gear/")),
    (r'^(?P<slug>[^/]+)/$',
     'django.views.generic.list_detail.object_detail',
     dict(slug_field='slug', queryset=Gear.objects.all())),
    (r'^(?P<slug>[^/]+)/edit_links/?$', 'gearspotting.gear.views.edit_links'),
    (r'^(?P<slug>[^/]+)/edit_photos/?$',
     'gearspotting.gear.views.edit_photos'),
    (r'^(?P<slug>[^/]+)/add_link/$', 'gearspotting.gear.views.add_link'),
    (r'^(?P<slug>[^/]+)/add_photo/$', 'gearspotting.gear.views.add_photo'),
)
