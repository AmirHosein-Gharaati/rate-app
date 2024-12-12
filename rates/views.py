from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RatingCreateSerializer, RatingSerializer
from .services import handle_rating
from .tasks import handle_computing_rating_averages


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
        handle_computing_rating_averages()
        return Response({"message": "successful"}, status=status.HTTP_200_OK)
