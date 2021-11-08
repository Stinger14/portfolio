from django.test import TestCase
from django.utils import timezone
from .models import PythonFeed,  TechFeed, RemoteJobsFeed, NbaFeed


class PythonFeedTests(TestCase):
    def setUp(self):
        self.pythonfeed = PythonFeed.objects.create(
            title="Awesome python content",
            description="Really cool stuff and tricks in python",
            pub_date=timezone.now(),
            link="https://realpython.com",
            image="https://image.somerandomsite.com",
            sourcefeed="Python content",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_pythonfeed_content(self):
        self.assertEqual(self.pythonfeed.description, "Really cool stuff and tricks in python")
        self.assertEqual(self.pythonfeed.link, "https://realpython.com")
        self.assertEqual(self.pythonfeed.guid, "de194720-7b4c-49e2-a05f-432436d3fetr")


    def test_pythonfeed_str_representation(self):
        self.assertEqual(str(self.pythonfeed), "Python content: Awesome python content")


class TechFeedTests(TestCase):
    def setUp(self):
        self.techfeed = TechFeed.objects.create(
            title="Awesome tech content",
            description="Digested tech news feed",
            pub_date=timezone.now(),
            link="https://www.techradar.com",
            image="https://image.somerandomsite.com",
            sourcefeed="Tech content",
            guid="de194585-7b4c-49e2-u5uf-432436d3tipb",
        )

    def test_pythonfeed_content(self):
        self.assertEqual(self.techfeed.description, "Digested tech news feed")
        self.assertEqual(self.techfeed.link, "https://www.techradar.com")
        self.assertEqual(self.techfeed.guid, "de194585-7b4c-49e2-u5uf-432436d3tipb")


    def test_pythonfeed_str_representation(self):
        self.assertEqual(str(self.techfeed), "Tech content: Awesome tech content")

