from django.urls import path

from rates.views import PostView, RateView

urlpatterns = [
    path('post', PostView.as_view(), name='post'),
    path('rate', RateView.as_view(), name='rate'),
]
