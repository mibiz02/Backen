from rest_framework import serializers
from .models import Movie
from .models import Movie_Comment

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Movie
        fields='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie_Comment
        fields = '__all__'
        read_only_fields = ('movie',)