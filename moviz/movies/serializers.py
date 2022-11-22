from rest_framework import serializers
from .models import Movie, Movie_Comment


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Movie
        fields='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie_Comment
        fields = ('content',)
        read_only_fields = ('movie',)