from django.core.management.base import BaseCommand
from gearspotting.musician.models import Musician
from gearspotting.gear.models import Gear
from json import loads


class Command(BaseCommand):
    def handle(self, *args, **options):
        dfile = open("tags.json", "rb")
        data = loads(dfile.read())

        for m in data['musicians']:
            musician = Musician.objects.get(id=m['id'])
            musician.tags.set(*m['tags'])

        for g in data['gear']:
            gear = Gear.objects.get(id=g['id'])
            gear.tags.set(*g['tags'])

