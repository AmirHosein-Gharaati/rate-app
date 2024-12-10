from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
