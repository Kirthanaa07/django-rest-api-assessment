from rest_framework import serializers
from tunaapi.models import Artist, Song
from tunaapi.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "description")

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "title", "artist", "album", "length")

class GenreWithSongsSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    
    class Meta:
        model = Genre
        fields = ("id", "description", "songs")
        
class ArtistWithSongsSerializer(serializers.ModelSerializer):
    song_count = serializers.IntegerField(source='songs.count', default=None)
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ("id", "name", "age", "bio", "song_count", "songs")
        
class ArtistSerializer(serializers.ModelSerializer):
    # song_count = serializers.IntegerField(source='songs.count', default=None)

    class Meta:
        model = Artist
        fields = ("id", "name", "age", "bio")


class SongWithGenresSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    artist = ArtistSerializer()

    class Meta:
        model = Song
        fields = ("id", "title", "artist", "album", "length", "genres")
        depth: 2
        
# class SongGenreSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = SongGenre
#     fields = ('genre')        
