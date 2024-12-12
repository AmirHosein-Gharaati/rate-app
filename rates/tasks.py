import datetime
from collections import defaultdict

from django.db.models import QuerySet

from rates.models import Post, Rating, RatingAverage
from rates.services import calculate_weighted_average


def handle_computing_rating_averages():
    ratings = Rating.objects.select_related('post').filter(computed=False)

    grouped_ratings = defaultdict(list)
    for rating in ratings:
        grouped_ratings[rating.post].append(rating)

    rating_averages = []

    for post, rating_list in grouped_ratings.items():
        count = len(rating_list)
        rating_sum = sum(rating.score for rating in ratings)
        average = round(rating_sum / count, 2)

        rating_averages.append(
            RatingAverage(
                post=post,
                rate_average=average,
            )
        )

    RatingAverage.objects.bulk_create(rating_averages)
    ratings.update(computed=True)


def handle_updating_post_rating():
    posts = Post.objects.all()

    for post in posts:
        averages = RatingAverage.objects.filter(post=post).order_by('-from_time')

        if len(averages) > 0:
            total_average = calculate_weighted_average(averages)

            post.rate_average = total_average
            post.user_count = Rating.objects.filter(post=post).count()
            post.save()
