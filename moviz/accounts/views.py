from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from .models import User
from movies.models import Movie
from .serializers import UserSerializer,likeMovieSerializer
from movies.serializers import MovieSerializer

@api_view(['GET'])
def user_profile(request):
    user = User.objects.get(pk=request.user.pk)
    serializer = UserSerializer(user)
    print(user)
    print(user.like_movies.all)
    print('-'*50)
    return Response(serializer.data)

@api_view(['GET'])
def user_like_movie(request):
    user = User.objects.get(pk=request.user.pk)
    movie = Movie.objects.filter(movie_like_users=user)
    serializer = likeMovieSerializer(movie, many=True)
    return Response(serializer.data)