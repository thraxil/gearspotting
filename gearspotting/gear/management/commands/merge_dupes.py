import collections
from typing import Any

from django.core.management.base import BaseCommand

from gearspotting.gear.models import Gear


class Command(BaseCommand):
    def handle(self, *args: Any, **kwargs: Any) -> None:
        all_slugs = [g.slug for g in Gear.objects.all()]
        dup_slugs = [
            s for s, c in collections.Counter(all_slugs).items() if c > 1
        ]
        for s in dup_slugs:
            print(s)
            gdupes = Gear.objects.filter(slug=s)
            keep = gdupes[0]
            print(gdupes.count())
            for g in gdupes[1:]:
                for p in g.gearphoto_set.all():
                    p.gear = keep
                    p.save()
                for mg in g.musiciangear_set.all():
                    mg.gear = keep
                    mg.save()
                g.delete()
