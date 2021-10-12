from django.db import models
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])
