from posts.models import Post
from posts.services import calculate_weighted_average
from rates.models import RatingAverage, Rating


def handle_updating_post_rating():
    posts = Post.objects.all()

    posts_to_update = []

    for post in posts:
        averages = RatingAverage.objects.filter(post=post).order_by('-created_at')

        if averages.exists():
            total_average = calculate_weighted_average(averages)

            post.rate_average = total_average
            post.user_count = Rating.objects.filter(post=post, computed=True).count()

            posts_to_update.append(post)

    if posts_to_update:
        Post.objects.bulk_update(posts_to_update, ['rate_average', 'user_count'])