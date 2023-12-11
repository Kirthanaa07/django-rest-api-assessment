from django.db import models

from tunaapi.models.genres import Genre
from .artists import Artist


class Song(models.Model):
    artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    length = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name="songs")
