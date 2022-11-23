from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Streamer(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Genre(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=50)
    imdb = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='movie_images/', null=True)
    streamer = models.ForeignKey(Streamer, on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.movie.title + ' ' + str(self.stars)
    