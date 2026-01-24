from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from gearspotting.gear.models import Gear
from gearspotting.manufacturer.models import Manufacturer


class ManufacturerViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.manufacturer = Manufacturer.objects.create(name="Fender")

    def test_list_view(self):
        response = self.client.get("/manufacturer/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "manufacturer/manufacturer_list.html"
        )
        self.assertIn(self.manufacturer, response.context["object_list"])

    def test_detail_view(self):
        response = self.client.get(self.manufacturer.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "manufacturer/manufacturer_detail.html"
        )
        self.assertEqual(response.context["object"], self.manufacturer)

    def test_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/manufacturer/create/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/manufacturer/create/", {"name": "Gibson"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Manufacturer.objects.filter(name="Gibson").exists())

    def test_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/manufacturer/{self.manufacturer.slug}/update/"
        response = self.client.post(url, {"name": "Fender Updated"})
        self.manufacturer.refresh_from_db()
        self.assertRedirects(response, self.manufacturer.get_absolute_url())
        self.assertEqual(self.manufacturer.name, "Fender Updated")

    def test_add_link_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/manufacturer/{self.manufacturer.slug}/add_link/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            url, {"title": "test link", "url": "https://example.com"}
        )
        self.assertRedirects(response, self.manufacturer.get_absolute_url())
        self.assertEqual(self.manufacturer.links.count(), 1)

    def test_delete_view_post(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/manufacturer/{self.manufacturer.slug}/delete/"
        response = self.client.post(url)
        self.assertRedirects(response, "/manufacturer/")
        self.assertFalse(
            Manufacturer.objects.filter(pk=self.manufacturer.pk).exists()
        )

    def test_add_gear_view_post(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/manufacturer/{self.manufacturer.slug}/add_gear/"
        response = self.client.post(url, {"name": "Stratocaster"})
        self.assertRedirects(response, self.manufacturer.get_absolute_url())
        self.assertTrue(Gear.objects.filter(name="Stratocaster").exists())
        gear = Gear.objects.get(name="Stratocaster")
        self.assertEqual(gear.manufacturer, self.manufacturer)
