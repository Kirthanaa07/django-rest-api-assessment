# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from tunaapi.models import SongGenre, Song, Genre
# from tunaapi.serializers import SongGenreSerializer

# class SongGenreView(ViewSet):
  
#   def retrieve(self, request, pk):
    
#     try:
#       song_genre = SongGenre.objects.get(pk=pk)
#       serializer = SongGenreSerializer(song_genre)
#       return Response(serializer.data)
#     except SongGenre.DoesNotExist as ex:
#       return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
#   def list(self, request):
#     song_genre = SongGenre.objects.all()
#     serializer = SongGenreSerializer(song_genre, many=True)
#     return Response(serializer.data)
  
#   def create(self, request):
    
#     song = Song.objects.get(pk=request.data["song_id"])
#     genre = Genre.objects.get(pk=request.data["genre_id"])
    
#     song_genre = SongGenre.objects.create(
#       song=song,
#       genre=genre,
#     )
#     serializer = SongGenreSerializer(song)
#     return Response(serializer.data)
  
#   def update(self, request, pk):
    
#     song_genre = SongGenre.objects.get(pk=pk)
    
#     song = Song.objects.get(pk=request.data["song"])
#     genre = Genre.objects.get(pk=request.data["genre"])
    
#     song_genre.song = song
#     song_genre.genre = genre
    
#     song_genre.save()
    
#     return Response(None, status=status.HTTP_204_NO_CONTENT)
  
#   def destroy(self, request, pk):
    
#     song_genre = SongGenre.objects.get(pk=pk)
#     song_genre.delete()
    
#     return Response(None, status=status.HTTP_204_NO_CONTENT)