from unittest.mock import Mock, patch

from django.contrib.auth.models import User
from django.test import TestCase

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
