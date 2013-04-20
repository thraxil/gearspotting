from django.db import models
from django.contrib.auth.models import User


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
