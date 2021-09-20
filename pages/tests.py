from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomePageTest(SimpleTestCase):

    def test_homepage_status_code(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_homepage_url_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_homepage_template(self):
        res = self.client.get('/')
        self.assertTemplateUsed(res, 'home.html')

    def test_homepage_contains_correct_html(self):
        res = self.client.get('/')
        self.assertContains(res, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        res = self.client.get('/')
        self.assertNotContains(res, 'hey, i should not be on the page!')
