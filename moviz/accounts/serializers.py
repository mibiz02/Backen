from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User
from movies.models import Movie


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=128)
    MBTI_type = serializers.CharField(required=False, max_length=4)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['MBTI_type'] = self.validated_data.get('MBTI_type', '')
        return data_dict


class MovieSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id',)

class UserSerializer(serializers.ModelSerializer):
    # like_movies_title = MovieSetSerializer(read_only=True)
    # like_movies_title = serializers.CharField(source='like_movies.all', read_only=True)
    # like_movies_title = serializers.ListField(source='like_movies.all', read_only=True)
    # count_like_movies_set = MovieSerializer(read_only=True, many=True)
    # count_like_movies
    # like_movies


    class Meta:
        model = User
        fields=('username','email','nickname','date_joined','MBTI_type',)
        # fields=('nickname','like_movies',)

class likeMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)