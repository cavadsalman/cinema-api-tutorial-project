from django.urls import path
from . import views

urlpatterns = [
    path('movie-list/', views.MovieListAV.as_view(), name='movie_list'),
    path('movie-list/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('review-list/', views.ReviewListAV.as_view(), name='review-list'),
    path('review-list-raw/', views.ReviewListAV.as_view(), name='review-list'),
    path('review-list/<int:pk>/', views.ReviewDetailAV.as_view(), name='review-detail')
]
