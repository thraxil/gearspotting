from django.core.management.base import BaseCommand
from gearspotting.musician.models import Musician
from gearspotting.gear.models import Gear
from tagging.models import Tag
from json import dumps


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = dict(musicians=[], gear=[])
        for m in Musician.objects.all():
            tags = Tag.objects.get_for_object(m)
            data['musicians'].append(
                dict(id=m.id, tags=[t.name for t in tags]))

        for g in Gear.objects.all():
            tags = Tag.objects.get_for_object(g)
            data['gear'].append(
                dict(id=g.id, tags=[t.name for t in tags])
                )
        with open("tags.json", "wb") as outfile:
            outfile.write(dumps(data))
