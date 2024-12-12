from celery.schedules import crontab

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_BEAT_SCHEDULE = {
    "compute_rate_averages_task": {
        "task": "tasks.tasks.compute_rate_averages",
        "schedule": crontab(minute="*/1"),
    },
    "compute_post_ratings_task": {
        "task": "tasks.tasks.compute_post_ratings",
        "schedule": crontab(minute="*/1"),
    },
}
