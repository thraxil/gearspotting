from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.contrib.syndication.views import FeedDoesNotExist
from models import Gear


class GearFeed(Feed):
    title = "Gearspotting Newest Gear"
    link = "/"
    description = ""
    feed_type = Atom1Feed

    def items(self):
        return Gear.objects.order_by('-added')[:20]
