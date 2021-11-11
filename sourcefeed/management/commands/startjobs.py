from django.core.management.base import BaseCommand

import feedparser
from dateutil.parser import parse

from sourcefeed.models import PythonFeed

def save_new_episodes(feed):
    """Saves new episodes to the database.

    Checks the episode GUID against the episodes currently stored in the
    database. If not found, then a new `Episode` is added to the database.

    Args:
        feed: requires a feedparser object
    """
    
    p_title = feed.channel.title
    p_image = feed.channel.image["href"]

    for item in feed.entries:
        if not PythonFeed.objects.filter(guid=item.guid).exists():
            podcast = PythonFeed(
                title=item.title,
                description=item.description,
                pub_date=parse(item.published),
                link=item.link,
                image=p_image,
                sourcefeed=p_title,
                guid=item.guid,
            )
            podcast.save()

def fetch_realpython_podcasts():
    _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(_feed)

def fetch_talkpython_episodes():
    _feed = feedparser.parse("https://realpython.fm/episodes/rss")
    save_new_episodes(_feed)


class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_talkpython_episodes()
        fetch_realpython_podcasts()

