from django.db import models
from .genres import Genre
from .songs import Song

class SongGenre(models.Model):

    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="genres")
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="songs")