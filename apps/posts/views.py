from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from apps.api.pagination import get_paginated_response, LimitOffsetPagination
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer, PostCreateSerializer
from apps.posts.services import create_post


class PostView(APIView):

    @extend_schema(responses=PostSerializer)
    def get(self, request, *args, **kwargs):
        query = Post.objects.order_by('id')

        return get_paginated_response(
            request=request,
            pagination_class=LimitOffsetPagination,
            queryset=query,
            serializer_class=PostSerializer,
            view=self
        )

    @extend_schema(responses=PostSerializer, request=PostCreateSerializer)
    def post(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = create_post(title=serializer.validated_data.get('title'))
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
