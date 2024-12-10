from django.urls import path

from rates.views import PostView, RateView

urlpatterns = [
    path('posts', PostView.as_view(), name='posts'),
    path('rates', RateView.as_view(), name='rates'),
]
