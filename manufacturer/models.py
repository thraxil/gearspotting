from django.db import models
from django.contrib import admin
from link.models import Link, LinkInline
from django.forms import ModelForm
from django.contrib.contenttypes import generic
from django.template.defaultfilters import slugify



class Manufacturer(models.Model):
    name = models.CharField(default="",unique=True, max_length=256)
    slug = models.SlugField(max_length=256,editable=False)
    description = models.TextField(default="",blank=True)
    links = generic.GenericRelation(Link)
    added = models.DateTimeField(auto_now_add=True,editable=False)
    modified = models.DateTimeField(auto_now=True,editable=False)


    class Meta:
        ordering = ["name",]

    def get_absolute_url(self):
        return "/manufacturer/%s/" % self.slug

    def __unicode__(self):
        return self.name

    def links_formset(self):
        LinkFormset = generic.generic_inlineformset_factory(Link, extra=1)
        return LinkFormset(instance=self)

    def save(self):
        self.slug = slugify(self.name)[:256]
        super(Manufacturer, self).save()

    def add_gear_form(self):
        from gear.models import AddGearForm
        return AddGearForm

    def add_link_form(self):
        class LinkForm(ModelForm):
            class Meta:
                model = Link
                exclude = ('content_object','content_type','object_id')
        return LinkForm

    def type_display(self):
        return "Manufacturer"

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
#        exclude = ('slug',)

class ManufacturerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [LinkInline,]
admin.site.register(Manufacturer, ManufacturerAdmin)
