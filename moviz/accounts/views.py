from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

from .models import User
from movies.models import Movie, Movie_Comment
from mbti_compabilities.models import MBTI_Comment

from .serializers import UserSerializer, MovieCommentSerializer, MBTICommentSerailizer, likeMovieSerializer

@api_view(['GET'])
def user_profile(request):
    user = User.objects.get(pk=request.user.pk)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_movie_comment(request):
    movie_comment = Movie_Comment.objects.filter(user=request.user)
    serializer = MovieCommentSerializer(movie_comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_mbti_comment(request):
    mbti_comment = MBTI_Comment.objects.filter(user=request.user)
    serializer =MBTICommentSerailizer(mbti_comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def user_like_movie(request):
    movie= Movie.objects.filter(movie_like_users=request.user)
    serializer = likeMovieSerializer(movie, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)