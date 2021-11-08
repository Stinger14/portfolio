from django.contrib import admin

from .models import NbaFeed, TechFeed, RemoteJobsFeed, PythonFeed

@admin.register(NbaFeed)
class NbaFeedAdmin(admin.ModelAdmin):
    list_display = ("sourcefeed", "title", "pub_date")

@admin.register(TechFeed)
class TechFeedAdmin(admin.ModelAdmin):
    list_display = ("sourcefeed", "title", "pub_date")

@admin.register(RemoteJobsFeed)
class RemoteJobsFeedAdmin(admin.ModelAdmin):
    list_display = ("sourcefeed", "title", "pub_date")

@admin.register(PythonFeed)
class PythonFeedAdmin(admin.ModelAdmin):
    list_display = ("sourcefeed", "title", "pub_date")