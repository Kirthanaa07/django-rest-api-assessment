from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import SongGenre

class SongGenreView(ViewSet):
  def retrieve(self, request, pk):
    song_genre = SongGenre.objects.get(pk=pk)
    serializer = SongGenreSerializer(song_genre)
    return Response(serializer.data)
  
  def list(self, request):
    song_genre = SongGenre.objects.all()
    serializer = SongGenreSerializer(song_genre, many=True)
    return Response(serializer.data)
  
  
  
  def destroy(self, request, pk):
    song_genre = SongGenre.objects.get(pk=pk)
    song_genre.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class SongGenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = SongGenre
    fields = ('id', 'song', 'genre')  