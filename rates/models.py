from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    rate_average = models.FloatField(default=0.0)


class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.CharField()
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)