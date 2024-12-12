import logging

from celery import shared_task

log = logging.getLogger(__name__)


@shared_task
def compute_rate_averages():
    from rates.tasks import handle_computing_rating_averages

    log.info("starting computing")
    handle_computing_rating_averages()
    log.info("finished computing")


@shared_task
def compute_post_ratings():
    from posts.tasks import handle_updating_post_rating

    log.info("starting updating post ratings")
    handle_updating_post_rating()
    log.info("finished updating post ratings")
