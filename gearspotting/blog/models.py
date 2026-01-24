import re
from typing import Any

import markdown
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from gearspotting.gear.models import Gear
from gearspotting.musician.models import Musician


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    body = models.TextField(blank=True, default="")
    body_html = models.TextField(blank=True, default="")
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-published",)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse(
            "blog:blog_post_detail",
            args=[
                self.published.year,
                self.published.month,
                self.published.day,
                self.author.username,
                self.slug,
            ],
        )

    def save(self, *args: Any, **kwargs: Any) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def linked_body(self) -> str:
        return link_text(self.body)

    def render_body(self) -> None:
        self.body_html = markdown.markdown(self.linked_body())
        self.save()


class PostGear(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)


class PostMusician(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)


def link_text(text: str) -> str:
    """goes through the text, finding references
    to manufacturers, gear, or musicians, and links
    to their pages.

    [[manufacturer:Name]]
    [[gear:ManufacturerName:Name]]
    [[musician:Name]]

    """
    pattern = re.compile(r"(\[\[[^\]]+\]\])")
    pattern2 = re.compile(r"\[\[([^\]]+)\]\]")
    results = []
    for part in pattern.split(text):
        m = pattern2.match(part)
        if m:
            parts = m.groups()[0].split(":")
            if parts[0].lower() == "gear":
                manufacturer_name = parts[1]
                gear_name = parts[2]
                part = f'<a href="{reverse("gear:gear_detail", args=[slugify(gear_name)])}">{manufacturer_name} {gear_name}</a>'
            if parts[0].lower() == "manufacturer":
                manufacturer_name = parts[1]
                part = f'<a href="{reverse("manufacturer:manufacturer_detail", args=[slugify(manufacturer_name)])}">{manufacturer_name}</a>'
            if parts[0].lower() == "musician":
                musician_name = parts[1]
                part = f'<a href="{reverse("musician:musician_detail", args=[slugify(musician_name)])}">{musician_name}</a>'
        results.append(part)
    return "".join(results)
