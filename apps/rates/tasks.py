from collections import defaultdict

from apps.rates.models import RatingAverage
from apps.rates.services import get_not_computed_ratings_with_post


def handle_computing_rating_averages():
    ratings = get_not_computed_ratings_with_post()

    grouped_ratings = defaultdict(list)
    for rating in ratings:
        grouped_ratings[rating.post].append(rating)

    rating_averages = []

    for post, rating_list in grouped_ratings.items():
        count = len(rating_list)
        rating_sum = sum(rating.score for rating in rating_list)
        average = round(rating_sum / count, 2)

        rating_averages.append(
            RatingAverage(
                post=post,
                rate_average=average,
            )
        )

    RatingAverage.objects.bulk_create(rating_averages)
    ratings.update(computed=True)
