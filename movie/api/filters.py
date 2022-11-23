from django_filters import rest_framework as filters
from ..models import Review


class ReviewFilter(filters.FilterSet):
    stars_bigger = filters.NumberFilter('stars', 'gt')
    stars_little = filters.NumberFilter('stars', 'lt')
    
    class Meta:
        model = Review
        fields = ['stars', 'movie']