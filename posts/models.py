from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    rate_average = models.FloatField(default=None)
    user_count = models.IntegerField(default=None)
