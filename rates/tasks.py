import datetime

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
            RatingAverage(post=post, rate_average=average, from_time=one_minute_ago, to_time=now)
        )

    RatingAverage.objects.bulk_create(rating_averages)
