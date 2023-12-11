from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db.models import Count
from tunaapi.models import Artist
from tunaapi.serializers import ArtistWithSongsSerializer, ArtistSerializer


class ArtistView(ViewSet):
    def retrieve(self, request, pk):
        try:
            artists = Artist.objects.get(pk=pk)
            serializer = ArtistWithSongsSerializer(artists)
            return Response(serializer.data)
        except Artist.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def create(self, request):
        artist = Artist.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            bio=request.data["bio"],
        )

        serializer = ArtistSerializer(artist)
        return Response(None, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        artist.name = request.data["name"]
        artist.age = request.data["age"]
        artist.bio = request.data["bio"]
        artist.save()

        return Response(None, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        artist = Artist.objects.get(pk=pk)
        artist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
