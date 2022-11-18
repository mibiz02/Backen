from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import Movie
#from .models import Movie_Comment
from mbti_compabilities.models import Character

from .serializers import MovieSerializer
#from .serializers import CommentSerializer
from mbti_compabilities.serializer import CharacterSerializer

# Create your views here.
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def movie_lst(request):
    if request.method == 'GET':
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

#@api_view(['POST'])
#def comment_create(request, movie_pk):
    #movie = get_object_or_404(Movie, pk=movie_pk)
    #serializer = CommentSerializer(data=request.data)
    #if serializer.is_valid(raise_exception=True):
        #serializer.save(movie=movie)
        #return Response(serializer.data, status=status.HTTP_201_CREATED)
