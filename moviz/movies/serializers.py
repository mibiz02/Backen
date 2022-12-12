from rest_framework import serializers
from .models import Movie, Movie_Comment


class MovieSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='movie_like_users.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    MBTI_type = serializers.CharField(source='user.MBTI_type', read_only=True)
    comment_count = serializers.IntegerField(source='movie_comment_like_users.count', read_only=True)
    
    class Meta:
        model = Movie_Comment
        fields = '__all__'
        read_only_fields = ('movie','user','movie_comment_like_users',)