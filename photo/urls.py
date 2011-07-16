from django.conf.urls.defaults import *

from photo.models import Photo

info_dict = {
    'queryset': Photo.objects.all(),
}

urlpatterns = patterns('',
#                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
#                       (r'^create/?$', 'django.views.generic.create_update.create_object',
#                        dict(form_class=PhotoForm, post_save_redirect="/photo/") ),
#                       (r'^(?P<object_id>\d+)/update/?$', 'django.views.generic.create_update.update_object',
#                        dict(form_class=PhotoForm, post_save_redirect="/photo/") ),
#                       (r'^(?P<object_id>\d+)/delete/?$', 'django.views.generic.create_update.delete_object',
#                        dict(model=Photo, post_delete_redirect="/photo/") ),
                       (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
