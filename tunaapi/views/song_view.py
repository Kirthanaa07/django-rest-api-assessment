from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song
from tunaapi.models import Artist
from tunaapi.serializers import SongWithGenresSerializer, SongSerializer


class SongView(ViewSet):
    def retrieve(self, request, pk):
        try:
            song = Song.objects.get(pk=pk)
            serializer = SongWithGenresSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        songs = Song.objects.all()
        song_artist = request.query_params.get("artist_id", None)
        if song_artist is not None:
            songs = songs.filter(song_artist_id=song_artist)

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def create(self, request):
        song_artist = Artist.objects.get(pk=request.data[0]["artist_id"])

        song = Song.objects.create(
            title=request.data[0]["title"],
            artist=song_artist,
            album=request.data[0]["album"],
            length=request.data[0]["length"],
        )

        serializer = SongSerializer(song)
        return Response(None, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        song = Song.objects.get(pk=pk)

        song_artist = Artist.objects.get(pk=request.data[0]["artist_id"])
        song.title = request.data[0]["title"]
        song.album = request.data[0]["album"]
        song.length = request.data[0]["length"]

        song.artist = song_artist
        song.save()

        return Response(None, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
   



