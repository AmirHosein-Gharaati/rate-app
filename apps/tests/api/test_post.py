import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_getting_posts():
    api_client = APIClient()

    url_ = reverse("api:post")

    response = api_client.get(url_, content_type="application/json")

    assert response.status_code == 200
