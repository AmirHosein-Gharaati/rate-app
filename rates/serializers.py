from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingCreateSerializer(serializers.Serializer):
    post = serializers.IntegerField()
    user_id = serializers.CharField()
    score = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
