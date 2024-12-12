from django.db.models import QuerySet

from posts.models import Post
from rates.models import RatingAverage


def create_post(title: str) -> QuerySet[Post]:
    return Post.objects.create(title=title)


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
