from django.urls import path
from . import views

urlpatterns = [
    path('movie-list/', views.movie_list, name='movie_list'),
    path('movie-list/<int:pk>/', views.movie_detail, name='movie_detail'),
]
