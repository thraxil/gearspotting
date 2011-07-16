from django.conf.urls.defaults import *
from musiciangear.models import MusicianGear

info_dict = {
    'queryset': MusicianGear.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(model=MusicianGear, post_save_redirect="/musiciangear/") ),

                       (r'^(?P<object_id>\d+)/update/?$', 'django.views.generic.create_update.update_object',
                        dict(model=MusicianGear, post_save_redirect="/musiciangear/") ),

                       (r'^(?P<object_id>\d+)/delete/?$', 'django.views.generic.create_update.delete_object',
                        dict(model=MusicianGear, post_delete_redirect="/musiciangear/") ),
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', 
                        info_dict),
                       (r'^(?P<id>\d+)/edit_links/?$', 'musiciangear.views.edit_links'),
                       (r'^(?P<id>\d+)/edit_photos/?$', 'musiciangear.views.edit_photos'),
                       (r'^(?P<id>\d+)/add_link/$', 'musiciangear.views.add_link'),
                       (r'^(?P<id>\d+)/add_photo/$', 'musiciangear.views.add_photo'),

)

