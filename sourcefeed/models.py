from django.db import models


class PythonFeed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    sourcefeed = models.CharField(max_length=100)
    guid = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.sourcefeed}: {self.title}"


class RemoteJobsFeed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    sourcefeed = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.sourcefeed}: {self.title}"


class NbaFeed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    sourcefeed = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.sourcefeed}: {self.title}"


class TechFeed(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    sourcefeed = models.CharField(max_length=100)
    guid = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.sourcefeed}: {self.title}"
