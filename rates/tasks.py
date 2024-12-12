import datetime

from django.db.models import QuerySet

from rates.models import Post, Rating, RatingAverage
from rates.services import calculate_weighted_average


def handle_computing_rating_averages():
    posts = Post.objects.all()

    now = datetime.datetime.now()
    one_minute_ago = now - datetime.timedelta(minutes=1)

    rating_averages = []

    for post in posts:
        ratings = Rating.objects.filter(post=post, updated_at__gte=one_minute_ago)

        count = len(ratings)
        if count == 0:
            continue

        rating_sum = sum(rating.score for rating in ratings)
        average = round(rating_sum / count, 2)

        rating_averages.append(
            RatingAverage(
                post=post,
                rate_average=average,
                from_time=one_minute_ago,
                to_time=now
            )
        )

    RatingAverage.objects.bulk_create(rating_averages)


def handle_updating_post_rating():
    posts = Post.objects.all()

    for post in posts:
        averages = RatingAverage.objects.filter(post=post).order_by('-from_time')

        if len(averages) > 0:
            total_average = calculate_weighted_average(averages)

            post.rate_average = total_average
            post.user_count = Rating.objects.filter(post=post).count()
            post.save()
