from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from apps.rates.models import Rating
from apps.posts.models import Post


def handle_rating(post_id: int, score: int, user_id: str) -> QuerySet[Rating]:
    post = get_object_or_404(Post, id=post_id)

    try:
        rating = Rating.objects.get(user_id=user_id)
        rating.score = score
        rating.save()
    except Rating.DoesNotExist:
        rating = Rating.objects.create(post=post, score=score, user_id=user_id)

    return rating
