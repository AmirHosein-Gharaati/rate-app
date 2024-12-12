from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from rates.models import Post, Rating, RatingAverage


def create_post(title: str) -> QuerySet[Post]:
    return Post.objects.create(title=title)


def handle_rating(post_id: int, score: int, user_id: str) -> QuerySet[Rating]:
    post = get_object_or_404(Post, id=post_id)

    try:
        rating = Rating.objects.get(user_id=user_id)
        rating.score = score
        rating.save()
    except Rating.DoesNotExist:
        rating = Rating.objects.create(post=post, score=score, user_id=user_id)

    return rating


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
