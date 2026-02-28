from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext

from gearspotting.blog.models import Post
from gearspotting.gear.models import Gear
from gearspotting.manufacturer.models import Manufacturer
from gearspotting.musician.models import Musician


class IndexViewPerfTestCase(TestCase):
    def setUp(self):
        # Create some background data to satisfy other parts of the view
        self.manufacturer = Manufacturer.objects.create(name="Fender")
        self.gear = Gear.objects.create(
            name="Stratocaster", manufacturer=self.manufacturer
        )
        self.musician = Musician.objects.create(name="Jimi Hendrix")

    def test_n_plus_one(self):
        # Create 1 post
        user1 = User.objects.create_user("u1", "u1@e.com", "p")
        Post.objects.create(author=user1, title="P1", body="B1")

        # Count queries for 1 post
        with CaptureQueriesContext(connection) as ctx1:
            self.client.get("/")
        count1 = len(ctx1.captured_queries)

        # Create another post with a different author
        user2 = User.objects.create_user("u2", "u2@e.com", "p")
        Post.objects.create(author=user2, title="P2", body="B2")

        # Count queries for 2 posts
        with CaptureQueriesContext(connection) as ctx2:
            self.client.get("/")
        count2 = len(ctx2.captured_queries)

        # If N+1 exists, count2 should be greater than count1
        # Specifically, count2 should be count1 + 1 (for the extra author fetch)

        # We expect count2 == count1 if the issue is fixed
        self.assertEqual(
            count1,
            count2,
            f"N+1 query detected! 1 post: {count1} queries, 2 posts: {count2} queries",
        )
