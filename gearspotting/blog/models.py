from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import re


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    body = models.TextField(blank=True, default="")
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published', )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%04d/%02d/%02d/%s/%s/" % (
            self.published.year,
            self.published.month,
            self.published.day,
            self.author.username,
            self.slug,
        )

    def linked_body(self):
        return link_text(self.body)


def link_text(text):
    """ goes through the text, finding references
    to manufacturers, gear, or musicians, and links
    to their pages.

    [[manufacturer:Name]]
    [[gear:ManufacturerName:Name]]
    [[musician:Name]]

    """
    pattern = re.compile(
        r'(\[\[[^\]]+\]\])')
    pattern2 = re.compile(
        r'\[\[([^\]]+)\]\]')
    results = []
    for part in pattern.split(text):
        m = pattern2.match(part)
        if m:
            parts = m.groups()[0].split(':')
            if parts[0].lower() == 'gear':
                manufacturer_name = parts[1]
                gear_name = parts[2]
                part = (
                    """<a href="/gear/%s/">%s %s</a>"""
                    % (slugify(gear_name),
                       manufacturer_name,
                       gear_name,
                       ))
            if parts[0].lower() == 'manufacturer':
                manufacturer_name = parts[1]
                part = (
                    """<a href="/manufacturer/%s/">%s</a>"""
                    % (slugify(manufacturer_name),
                       manufacturer_name)
                    )
            if parts[0].lower() == 'musician':
                musician_name = parts[1]
                part = (
                    """<a href="/musician/%s/">%s</a>"""
                    % (slugify(musician_name),
                       musician_name)
                    )

        results.append(part)
    return ''.join(results)
