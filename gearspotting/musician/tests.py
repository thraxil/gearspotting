from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from gearspotting.gear.models import Gear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.musician.models import Musician, MusicianTag
from gearspotting.tag.models import Tag


class MusicianViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.musician = Musician.objects.create(name="Jimi Hendrix")
        self.tag = Tag.objects.create(name="guitarist")
        MusicianTag.objects.create(musician=self.musician, tag=self.tag)
        self.manufacturer = Manufacturer.objects.create(name="Fender")
        self.gear = Gear.objects.create(
            name="Stratocaster", manufacturer=self.manufacturer
        )

    def test_list_view(self):
        response = self.client.get("/musician/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "musician/musician_list.html")
        self.assertIn(self.musician, response.context["object_list"])

    def test_detail_view(self):
        response = self.client.get(self.musician.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "musician/musician_detail.html")
        self.assertEqual(response.context["object"], self.musician)

    def test_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get("/musician/create/")
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            "/musician/create/", {"name": "Jimmy Page"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Musician.objects.filter(name="Jimmy Page").exists())

    def test_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musician/{self.musician.slug}/update/"
        response = self.client.post(url, {"name": "Jimi Hendrix Updated"})
        self.musician.refresh_from_db()
        self.assertRedirects(response, self.musician.get_absolute_url())
        self.assertEqual(self.musician.name, "Jimi Hendrix Updated")

    def test_tags_view(self):
        response = self.client.get("/musician/tag/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "musician/tags.html")
        self.assertIn(self.tag, response.context["tags"])

    def test_musician_tag_view(self):
        url = reverse("musician_tag_detail", kwargs={"tag": self.tag.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "musician/musician_tag_list.html")
        self.assertContains(response, self.musician.name)

    def test_add_link_view(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musician/{self.musician.slug}/add_link/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            url, {"title": "test link", "url": "https://example.com"}
        )
        self.assertRedirects(response, self.musician.get_absolute_url())
        self.assertEqual(self.musician.links.count(), 1)

    def test_delete_view_post(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musician/{self.musician.slug}/delete/"
        response = self.client.post(url)
        self.assertRedirects(response, "/musician/")
        self.assertFalse(Musician.objects.filter(pk=self.musician.pk).exists())

    def test_add_photo_view_get(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musician/{self.musician.slug}/add_photo/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_gear_view_post(self):
        self.client.login(username="testuser", password="testpassword")
        url = f"/musician/{self.musician.slug}/add_gear/"
        response = self.client.post(url, {"gear": self.gear.id})
        self.assertRedirects(response, self.musician.get_absolute_url())
        self.assertEqual(self.musician.musiciangear_set.count(), 1)
