from django.urls import path

from posts.views import PostView, CalculateWeightedAverageView
from rates.views import RateView, RatingAverageView

urlpatterns = [
    path('post', PostView.as_view(), name='post'),
    path('post/update-average', CalculateWeightedAverageView.as_view(), name='post-update-average'),
    path('rate', RateView.as_view(), name='rate'),
    path('rate-average', RatingAverageView.as_view(), name='rate-average'),
]