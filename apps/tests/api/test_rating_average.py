import json
import random

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from apps.posts.models import Post
from apps.tests.factory import generate_rating_with_random_user
from apps.rates.tasks import handle_computing_rating_averages
from apps.posts.tasks import handle_updating_post_rating


@pytest.mark.django_db
def test_rating_average_algorithm():
    api_client = APIClient()
    number_of_posts = 100
    post_ids = setup_posts(api_client, number_of_posts)
    first_post_id = post_ids[0]

    url_ = reverse("api:rate")

    for i in range(5):
        send_rating_five_for_all_posts(api_client, post_ids, url_)

        handle_computing_rating_averages()
        handle_updating_post_rating()

    for i in range(100):
        send_zero_or_one_rating(api_client, first_post_id, url_)

    handle_computing_rating_averages()
    handle_updating_post_rating()

    post = Post.objects.get(id=first_post_id)

    assert post.rate_average > 4


def send_zero_or_one_rating(api_client, post_id, url_):
    score = random.randint(0, 1)
    body = generate_rating_with_random_user(post_id, score)
    response = api_client.post(url_, json.dumps(body), content_type="application/json")
    assert response.status_code == 201


def send_rating_five_for_all_posts(api_client, post_ids, url_):
    for post_id in post_ids:
        body = generate_rating_with_random_user(post_id, 5)
        response = api_client.post(url_, json.dumps(body), content_type="application/json")
        assert response.status_code == 201


def setup_posts(api_client: APIClient, number_of_posts: int):
    url_ = reverse("api:post")

    post_ids = []

    for i in range(1, number_of_posts + 1):
        body = {"title": f"Post{i}"}
        response = api_client.post(url_, json.dumps(body), content_type="application/json")
        assert response.status_code == 201
        post_ids.append(response.data['id'])

    return post_ids
