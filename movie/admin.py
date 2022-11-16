from django.contrib import admin
from .models import Movie, Streamer, Genre, Review

# Register your models here.
admin.site.register(Streamer)
admin.site.register(Genre)

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]