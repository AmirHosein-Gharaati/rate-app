from django.urls import path

from rates.views import PostView

urlpatterns = [
    path('posts', PostView.as_view(), name='posts')
]
