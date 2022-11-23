from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import (
    Movie, MovieSerializer,
    Review, ReviewSerializer
)
from rest_framework import status, generics, filters, parsers
from django.shortcuts import get_object_or_404
from .paginations import StandardPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import ReviewPermission
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ReviewFilter
from rest_framework.throttling import AnonRateThrottle

class ReviewListAV(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['stars', 'movie', 'created', 'user']
    filterset_class = ReviewFilter
    search_fields = ['comment', 'movie__title']
    ordering_fields = ['created', 'stars']
    
    
@api_view(['GET'])
def reivew_list(request):
    reviews = Review.objects.all()
    paginator = StandardPagination()
    page_reviews = paginator.paginate_queryset(reviews, request, reivew_list)
    serializer = ReviewSerializer(page_reviews, many=True)
    return paginator.get_paginated_response(serializer.data)
    
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [ReviewPermission]

class MovieListAV(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    throttle_classes = [AnonRateThrottle]

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(instance=movies, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAdminUser])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        serializer = MovieSerializer(instance=movie, context={'request': request} )
        return Response(serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieSerializer(instance=movie, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = MovieSerializer(instance=movie, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)