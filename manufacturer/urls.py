from django.conf.urls.defaults import *

from manufacturer.models import Manufacturer, ManufacturerForm

info_dict = {
    'queryset': Manufacturer.objects.all(),
}

urlpatterns = patterns('',
                       (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
                       (r'^create/?$', 'django.views.generic.create_update.create_object',
                        dict(form_class=ManufacturerForm, post_save_redirect="/manufacturer/") ),
                       (r'^(?P<slug>[^/]+)/update/?$', 'django.views.generic.create_update.update_object',
                        dict(form_class=ManufacturerForm, post_save_redirect="/manufacturer/") ),
                       (r'^(?P<slug>[^/]+)/delete/?$', 'django.views.generic.create_update.delete_object',
                        dict(model=Manufacturer, post_delete_redirect="/manufacturer/") ),
                       (r'^(?P<slug>[^/]+)/edit_links/?$', 'manufacturer.views.edit_links'),
                       (r'^(?P<slug>[^/]+)/add_gear/$', 'manufacturer.views.add_gear'),
                       (r'^(?P<slug>[^/]+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
                       (r'^(?P<slug>[^/]+)/add_link/$', 'manufacturer.views.add_link'),
)
