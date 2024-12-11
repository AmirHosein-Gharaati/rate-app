from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, PostCreateSerializer, RatingCreateSerializer, RatingSerializer
from .models import Post
from .services import create_post, handle_rating
from .tasks import compute_rating_averages


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


class RateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RatingCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        rate = handle_rating(
            user_id=serializer.validated_data.get('user_id'),
            post_id=serializer.validated_data.get('post'),
            score=serializer.validated_data.get('score')
        )
        return Response(RatingSerializer(rate).data, status=status.HTTP_201_CREATED)


# TODO: should use async schedular for triggering the computation
class RatingAverageView(APIView):

    def post(self, request, *args, **kwargs):
        compute_rating_averages()
        return Response({"message": "successful"}, status=status.HTTP_200_OK)
