from django.db import models
from .genres import Genre
from .songs import Song


# class Song_Genres(models.Model):
#     song = models.ForeignKey(Song, on_delete=models.CASCADE)
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
