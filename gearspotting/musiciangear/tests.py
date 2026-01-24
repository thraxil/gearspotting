from django.contrib.auth.models import User
from django.test import TestCase

from gearspotting.gear.models import Gear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.musician.models import Musician
from gearspotting.musiciangear.models import MusicianGear


class MusicianGearViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.manufacturer = Manufacturer.objects.create(name="Fender")
        self.gear = Gear.objects.create(
            name="Stratocaster", manufacturer=self.manufacturer
        )
        self.musician = Musician.objects.create(name="Jimi Hendrix")
        self.musiciangear = MusicianGear.objects.create(
            musician=self.musician, gear=self.gear
        )

    def test_list_view(self):
        response = self.client.get("/musiciangear/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "musiciangear/musiciangear_list.html"
        )
        self.assertIn(self.musiciangear, response.context["object_list"])

    def test_detail_view(self):
        response = self.client.get(self.musiciangear.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "musiciangear/musiciangear_detail.html"
        )
        self.assertEqual(response.context["object"], self.musiciangear)

    def test_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/musiciangear/create/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/musiciangear/create/",
            {
                "musician": self.musician.id,
                "gear": self.gear.id,
                "description": "test",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            MusicianGear.objects.filter(description="test").exists()
        )

    def test_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musiciangear/{self.musiciangear.id}/update/"
        response = self.client.post(
            url,
            {
                "musician": self.musician.id,
                "gear": self.gear.id,
                "description": "updated",
            },
        )
        self.assertRedirects(response, self.musiciangear.get_absolute_url())
        self.musiciangear.refresh_from_db()
        self.assertEqual(self.musiciangear.description, "updated")

    def test_delete_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musiciangear/{self.musiciangear.id}/delete/"
        response = self.client.post(url)
        self.assertRedirects(response, "/musiciangear/")
        self.assertFalse(
            MusicianGear.objects.filter(pk=self.musiciangear.pk).exists()
        )

    def test_add_link_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musiciangear/{self.musiciangear.id}/add_link/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            url, {"title": "test link", "url": "https://example.com"}
        )
        self.assertRedirects(response, self.musiciangear.get_absolute_url())
        self.assertEqual(self.musiciangear.links.count(), 1)
