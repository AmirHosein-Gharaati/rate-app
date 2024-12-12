from django.urls import path

from posts.views import PostView
from rates.views import RateView

urlpatterns = [
    path('post', PostView.as_view(), name='post'),
    path('rate', RateView.as_view(), name='rate'),
]
