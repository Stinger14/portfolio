from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.res = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.res.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.res, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.res, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.res, 'hey, i should not be on the page!')
