from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Project, Review


class ProjectTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='testpass123'
        )

        self.project = Project.objects.create(
            title='Url Shortner',
            description='More human readable link names',
        )

        self.review = Review.objects.create(
            project=self.project,
            author=self.user,
            review='An excellent review',
        )

    def test_project_listing(self):
        self.assertEqual(f'{self.project.title}', 'Url Shortner')
        self.assertEqual(f'{self.project.description}', 'More human readable link names')

    def test_project_list_view(self):
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Url Shortner')
        self.assertTemplateUsed(response, 'projects/project_list.html')

    def test_project_detail_view(self):
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get('/projects/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Url Shortner')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'projects/project_detail.html')
