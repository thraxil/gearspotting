from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from gearspotting.gear.models import Gear, GearTag
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.photo.models import Photo
from gearspotting.tag.models import Tag


class GearViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.manufacturer = Manufacturer.objects.create(name="Fender")
        self.gear = Gear.objects.create(
            name="Stratocaster", manufacturer=self.manufacturer
        )
        self.tag = Tag.objects.create(name="guitar")
        GearTag.objects.create(gear=self.gear, tag=self.tag)

    def test_index_view(self):
        response = self.client.get(reverse("gear:gear_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gear/index.html")

    def test_gear_detail_view(self):
        response = self.client.get(self.gear.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gear/gear_detail.html")
        self.assertEqual(response.context["object"], self.gear)

    def test_tags_view(self):
        response = self.client.get(reverse("gear:gear_tags"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gear/tags.html")
        self.assertContains(response, self.tag.name)

    def test_gear_tag_view(self):
        url = reverse("gear:gear_tag_detail", kwargs={"tag": self.tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gear/gear_tag_list.html")
        self.assertContains(response, self.gear.name)

    def test_create_gear_view_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            reverse("gear:gear_create"),
            {
                "name": "Telecaster",
                "manufacturer": self.manufacturer.id,
                "description": "A solid body electric guitar.",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Gear.objects.filter(name="Telecaster").exists())
        tele = Gear.objects.get(name="Telecaster")
        self.assertEqual(tele.manufacturer, self.manufacturer)
        self.assertRedirects(response, tele.get_absolute_url())

    def test_update_gear_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("gear:gear_update", kwargs={"slug": self.gear.slug})
        response = self.client.post(
            url,
            {
                "name": "Stratocaster Updated",
                "manufacturer": self.manufacturer.id,
                "description": "Updated",
            },
        )
        self.gear.refresh_from_db()
        self.assertRedirects(response, self.gear.get_absolute_url())
        self.assertEqual(self.gear.name, "Stratocaster Updated")

    def test_delete_gear_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("gear:gear_delete", kwargs={"slug": self.gear.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "gear/gear_confirm_delete.html")
        response = self.client.post(url)
        self.assertRedirects(response, reverse("gear:gear_index"))
        self.assertFalse(Gear.objects.filter(pk=self.gear.pk).exists())

    def test_add_link_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("gear:gear_add_link", kwargs={"slug": self.gear.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            url, {"title": "test link", "url": "https://example.com"}
        )
        self.assertRedirects(response, self.gear.get_absolute_url())
        self.assertEqual(self.gear.links.count(), 1)

    def test_add_photo_view_get(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("gear:gear_add_photo", kwargs={"slug": self.gear.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
