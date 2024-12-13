from django.db.models import QuerySet

from apps.posts.models import Post
from apps.rates.models import RatingAverage, Rating


def create_post(title: str) -> QuerySet[Post]:
    return Post.objects.create(title=title)


def get_rating_averages_order_by_created_at(post: Post) -> QuerySet[RatingAverage]:
    return RatingAverage.objects.filter(post=post).order_by('-created_at')


def get_ratings_count(post: Post) -> int:
    return Rating.objects.filter(post=post, computed=True).count()


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
