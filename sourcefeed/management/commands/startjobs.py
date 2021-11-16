# Std library
import logging

# Django
from django.core.management.base import BaseCommand
from django.conf import settings

# Third party
import feedparser
from dateutil.parser import parse
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from sourcefeed.models import PythonFeed


logger = logging.getLogger(__name__)

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
            feed = PythonFeed(
                title=item.title,
                description=item.description,
                pub_date=parse(item.published),
                link=item.link,
                image=p_image,
                sourcefeed=p_title,
                guid=item.guid,
            )
            feed.save()

def fetch_realpython_podcasts():
    _feed = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
    save_new_episodes(_feed)

def fetch_talkpython_episodes():
    _feed = feedparser.parse("https://talkpython.fm/episodes/rss")
    save_new_episodes(_feed)

def delete_old_job_executions(max_age=604_800):
    """Deletes all apscheduler job execution logs older than `max_age`.
       Note: 604,800 seconds is equal to 1 week.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler"

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            fetch_realpython_podcasts,
            trigger="interval",
            minutes=2,
            id="The Real Python Podcast",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: The Real Python Podcast")

        scheduler.add_job(
            fetch_talkpython_episodes,
            trigger="interval",
            minutes=2,
            id="Talk Python Feed",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: Talk Python Feed")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"), # midnight on monday
            id="Deletes Old Jobs Executions",
            max_instances=1,
            replace_existing=True,
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shutdown successfully!")

    
