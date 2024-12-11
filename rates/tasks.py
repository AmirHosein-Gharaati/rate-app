import datetime

from django.db.models import QuerySet

from rates.models import Post, Rating, RatingAverage


def compute_rating_averages():
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
                to_time=now,
                user_count=count
            )
        )

    RatingAverage.objects.bulk_create(rating_averages)


def calculate_weighted_average(averages: QuerySet[RatingAverage]):
    weighted_sum = 0
    weight_total = 0
    weight = 1

    for avg_data in averages:
        weighted_sum += avg_data.rate_average * weight
        weight_total += weight
        weight += 1

    rate_average = round(weighted_sum / weight_total if weight_total else 0, 2)

    return rate_average


def handle_updating_post_rating():
    posts = Post.objects.all()

    for post in posts:
        averages = RatingAverage.objects.filter(post=post).order_by('-from_time')

        if len(averages) > 0:
            total_average = calculate_weighted_average(averages)

            post.rate_average = total_average
            post.user_count = Rating.objects.filter(post=post).count()
            post.save()
