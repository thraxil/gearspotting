from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.text import slugify

from gearspotting.blog.models import Post


class BlogViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "testuser", "test@example.com", "testpassword"
        )
        self.post = Post.objects.create(
            author=self.user,
            title="Test Post",
            slug="test-post",
            body="This is a test post.",
        )

    def test_index_view(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")
        self.assertIn("posts", response.context)

    def test_add_post_view_post_unauthenticated_fails(self):
        response = self.client.post(
            "/blog/post/", {"title": "New Title", "body": "New Body"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/blog/post/")
        self.assertEqual(Post.objects.count(), 1)

    def test_add_post_view_post_empty_body(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            "/blog/post/", {"title": "New Title", "body": ""}
        )
        self.assertRedirects(response, "/blog/post/")
        self.assertEqual(Post.objects.count(), 1)

    def test_add_post_view_post_success(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(
            "/blog/post/", {"title": "New Title", "body": "New Body"}
        )
        self.assertRedirects(response, "/blog/")
        self.assertEqual(Post.objects.count(), 2)
        new_post = Post.objects.get(title="New Title")
        self.assertEqual(new_post.body, "New Body")
        self.assertEqual(new_post.author, self.user)
        self.assertEqual(new_post.slug, slugify("New Title"))

    def test_post_view_success(self):
        p = self.post
        url = (
            f"/blog/{p.published.year}/{p.published.month:02d}/"
            f"{p.published.day:02d}/{p.author.username}/{p.slug}/"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post.html")
        self.assertEqual(response.context["post"], self.post)

    def test_post_view_not_found(self):
        p = self.post
        url = (
            f"/blog/{p.published.year}/{p.published.month:02d}/"
            f"{p.published.day:02d}/{p.author.username}/wrong-slug/"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        url = (
            f"/blog/{p.published.year}/{p.published.month:02d}/"
            f"{p.published.day:02d}/wronguser/{p.slug}/"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
