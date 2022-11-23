from rest_framework import serializers
from django.db.models import Avg
from ..models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    movie_name = serializers.StringRelatedField(source="movie")
    
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # reviews = serializers.StringRelatedField(many=True, read_only=True)
    # reviews = serializers.SlugRelatedField(many=True, read_only=True, slug_field='comment')
    # reviews = ReviewSerializer(many=True)
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
    average_star = serializers.SerializerMethodField()
    
    def validate_imdb(self, value):
        if not 0 <= value <= 10:
            raise serializers.ValidationError('IMDB deyeri 0 ve 10 arasi olmalidir!')
        return value
    
    def validate(self, data):
        if data.get('imdb') < len(data.get('title')):
            raise serializers.ValidationError('imdb adin uzunlugundan az ola bilmez!')
        return data
    
    def get_average_star(self, obj):
        return obj.reviews.aggregate(Avg('stars')).get('stars__avg')
    
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1