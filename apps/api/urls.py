from django.urls import path

from apps.posts.views import PostView
from apps.rates.views import RateView

urlpatterns = [
    path('post', PostView.as_view(), name='post'),
    path('rate', RateView.as_view(), name='rate'),
]
