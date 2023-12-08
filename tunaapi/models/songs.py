from django.db import models
from .artists import Artist

class Song(models.Model):
  
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    length = models.IntegerField()