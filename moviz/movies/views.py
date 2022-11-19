from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Movie
from mbti_compabilities.models import Character

from .serializers import MovieSerializer
from mbti_compabilities.serializer import CharacterSerializer

# Create your views here.
@api_view(['GET'])
def movie_lst(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_mbti_character(request, movie_pk):
    a = Movie.objects.filter(pk=movie_pk)
    characters = Character.objects.filter(movie_title=(a[0].movie_title))
    # characters = Character.objects.filter(movie_title='The Godfather')
    serializer  = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
