import logging

from celery import shared_task

log = logging.getLogger(__name__)


@shared_task
def compute_rate_averages():
    from apps.rates.tasks import handle_computing_rating_averages

    log.info("starting computing rating averages")
    handle_computing_rating_averages()
    log.info("finished computing rating averages")


@shared_task
def compute_post_ratings():
    from apps.posts.tasks import handle_updating_post_rating

    log.info("starting updating post ratings")
    handle_updating_post_rating()
    log.info("finished updating post ratings")
