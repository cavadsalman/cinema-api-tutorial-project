from django.db import models

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
    imdb = models.FloatField()
    image_url = models.URLField(max_length=200)
    streamer = models.ForeignKey(Streamer, on_delete=models.SET_NULL, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.movie.title + ' ' + str(self.stars)
    