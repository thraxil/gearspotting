from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from .models import Post


class BlogFeed(Feed):
    title = "Gearspotting Blog"
    link = "/"
    description = ""
    feed_type = Atom1Feed

    def items(self):
        return Post.objects.order_by('-published')[:20]
