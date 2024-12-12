from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer, PostCreateSerializer
from posts.services import create_post
from posts.tasks import handle_updating_post_rating


class PostView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = create_post(title=serializer.validated_data.get('title'))
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: should use async schedular for triggering the computation
class CalculateWeightedAverageView(APIView):
    def post(self, request, *args, **kwargs):
        handle_updating_post_rating()
        return Response({"message": "successful"}, status=status.HTTP_200_OK)
