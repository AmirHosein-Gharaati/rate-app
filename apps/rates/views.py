from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .serializers import RatingCreateSerializer, RatingSerializer
from .services import handle_rating


class RateView(APIView):

    @extend_schema(responses=RatingSerializer, request=RatingCreateSerializer)
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
