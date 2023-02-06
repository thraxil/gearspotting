from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from .models import Musician


class MusicianFeed(Feed):
    title = "Gearspotting Newest Musicians"
    link = "/"
    description = ""
    feed_type = Atom1Feed

    def items(self):
        return Musician.objects.order_by("-added")[:20]
