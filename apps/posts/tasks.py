from apps.posts.models import Post
from apps.posts.services import (
    calculate_weighted_average,
    get_rating_averages_order_by_created_at,
    get_ratings_count
)


def handle_updating_post_rating():
    # TODO: the function can be optimized to only update the posts that have new rating average
    posts = Post.objects.all()

    posts_to_update = []

    for post in posts:
        averages = get_rating_averages_order_by_created_at(post)

        if averages.exists():
            total_average = calculate_weighted_average(averages)

            post.rate_average = total_average
            post.user_count = get_ratings_count(post)

            posts_to_update.append(post)

    if posts_to_update:
        Post.objects.bulk_update(posts_to_update, ['rate_average', 'user_count'])
