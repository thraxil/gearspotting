from unittest.mock import Mock, patch

from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.urls import reverse

from gearspotting.gear.models import Gear, GearPhoto
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.musician.models import Musician, MusicianPhoto
from gearspotting.musiciangear.models import MusicianGear, MusicianGearPhoto
from gearspotting.photo.models import Photo


class PhotoViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.photo = Photo.objects.create()

    def test_detail_view(self):
        response = self.client.get(f"/photos/{self.photo.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "photo/photo_detail.html")
        self.assertEqual(response.context["object"], self.photo)

    def test_import_photo_view_get(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/photos/import/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "photo/import_photo.html")

    @patch("gearspotting.photo.views.requests")
    def test_import_photo_view_post(self, mock_requests):
        self.client.login(username="testuser", password="testpassword")
        mock_requests.get.return_value.iter_content.return_value = [
            b"test image data"
        ]
        mock_requests.post.return_value.json.return_value = {
            "hash": "test_hash"
        }

        response = self.client.post(
            "/photos/import/",
            {
                "url": "https://example.com/test.jpg",
                "caption": "test caption",
                "musicians": "Jimi Hendrix",
                "gear": "Fender:Stratocaster",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Photo.objects.filter(caption="test caption").exists())
        photo = Photo.objects.get(caption="test caption")
        self.assertEqual(photo.reticulum_key, "test_hash")


class PhotoNPlusOneTestCase(TestCase):
    def setUp(self):
        self.photo = Photo.objects.create()
        self.manufacturer = Manufacturer.objects.create(
            name="Test Manufacturer"
        )

        # Create 10 gears linked to the photo
        for i in range(10):
            gear = Gear.objects.create(
                name=f"Gear {i}", manufacturer=self.manufacturer
            )
            GearPhoto.objects.create(gear=gear, photo=self.photo)

        # Create 10 musicians linked to the photo
        for i in range(10):
            musician = Musician.objects.create(name=f"Musician {i}")
            MusicianPhoto.objects.create(musician=musician, photo=self.photo)

        # Create 10 musician gears linked to the photo with distinct owners and gears
        for i in range(10):
            owner = Musician.objects.create(name=f"Owner {i}")
            gear_item = Gear.objects.create(
                name=f"Owned Gear {i}", manufacturer=self.manufacturer
            )
            mg = MusicianGear.objects.create(
                musician=owner, gear=gear_item, description=f"MG {i}"
            )
            MusicianGearPhoto.objects.create(musiciangear=mg, photo=self.photo)

    def test_detail_view_queries(self):
        url = reverse("photo:photo_detail", args=[self.photo.id])

        with CaptureQueriesContext(connection) as ctx:
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertLess(len(ctx.captured_queries), 20)
