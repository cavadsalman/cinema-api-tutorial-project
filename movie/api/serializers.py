from rest_framework import serializers
from ..models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # reviews = serializers.StringRelatedField(many=True, read_only=True)
    # reviews = serializers.SlugRelatedField(many=True, read_only=True, slug_field='comment')
    reviews = ReviewSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1