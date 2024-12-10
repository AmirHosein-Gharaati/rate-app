from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from rates.models import Post, Rating


def create_post(title: str) -> QuerySet[Post]:
    return Post.objects.create(title=title)


def create_rate(post_id: int, score: int, user_id: str) -> QuerySet[Rating]:
    post = get_object_or_404(Post, id=post_id)
    return Rating.objects.create(post=post, score=score, user_id=user_id)
