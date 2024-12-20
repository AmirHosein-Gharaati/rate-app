from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.posts.models import Post


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.CharField()
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    computed = models.BooleanField(default=False)


class RatingAverage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rate_average = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
