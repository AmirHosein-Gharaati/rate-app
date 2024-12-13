import json

import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_getting_posts():
    # setup
    api_client = APIClient()
    url_ = reverse("api:post")
    number_of_posts_to_insert = 10

    for i in range(1, number_of_posts_to_insert + 1):
        body = {"title": f"Post{i}"}
        response = api_client.post(url_, json.dumps(body), content_type="application/json")
        assert response.status_code == 201

    # when
    posts_response = api_client.get(url_, content_type="application/json")

    # then
    assert posts_response.status_code == 200
    assert posts_response.data['count'] == number_of_posts_to_insert
    assert posts_response.data['limit'] == number_of_posts_to_insert
    posts = posts_response.data['results']
    assert posts[0]['id'] == 1
