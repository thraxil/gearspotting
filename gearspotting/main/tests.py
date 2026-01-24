from django.contrib.auth.models import User
from django.test import TestCase

from gearspotting.blog.models import Post
from gearspotting.gear.models import Gear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.musician.models import Musician


class MainViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.manufacturer = Manufacturer.objects.create(name="Fender")
        self.gear = Gear.objects.create(
            name="Stratocaster", manufacturer=self.manufacturer
        )
        self.musician = Musician.objects.create(name="Jimi Hendrix")
        self.post = Post.objects.create(
            author=self.user, title="Test Post", body="Test body"
        )

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "homepage.html")
        self.assertIn("newest_gear", response.context)
        self.assertIn("newest_musicians", response.context)
        self.assertIn("newest_posts", response.context)
        self.assertIn(self.gear, response.context["newest_gear"])
        self.assertIn(self.musician, response.context["newest_musicians"])
        self.assertIn(self.post, response.context["newest_posts"])

    def test_search_view_no_query(self):
        response = self.client.get("/search/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/search.html")
        self.assertEqual(response.context["q"], None)

    def test_search_view_with_query(self):
        response = self.client.get("/search/", {"q": "strat"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/search.html")
        self.assertEqual(response.context["q"], "strat")
        self.assertIn("results", response.context)
        self.assertIn(self.gear, response.context["results"]["gear"])
