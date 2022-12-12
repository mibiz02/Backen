from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User
from movies.models import Movie, Movie_Comment
from mbti_compabilities.models import MBTI_Comment


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=128)
    MBTI_type = serializers.CharField(required=False, max_length=4)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['MBTI_type'] = self.validated_data.get('MBTI_type', '')
        return data_dict


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields='__all__'


class MovieCommentSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    
    class Meta:
        model = Movie_Comment
        fields = '__all__'
        

class MBTICommentSerailizer(serializers.ModelSerializer):
    mbti_page = serializers.CharField(source='mbti_type.letter', read_only=True)
    
    class Meta:
        model = MBTI_Comment
        fields = '__all__'
        
class likeMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        
        