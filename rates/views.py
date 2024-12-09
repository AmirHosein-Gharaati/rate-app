from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer


@api_view(['GET'])
def get_posts(request):
    fake_posts = [PostSerializer({"title": "test", "rate_average": 4.5}).data]
    return Response(fake_posts)
