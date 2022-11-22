from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Movie, Movie_Comment
from mbti_compabilities.models import Character

from .serializers import MovieSerializer,CommentSerializer
from mbti_compabilities.serializer import CharacterSerializer

# Create your views here.
@api_view(['GET'])
def movie_lst(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_mbti_character(request, movie_pk):
    this_movie = Movie.objects.filter(pk=movie_pk)
    print(this_movie)
    characters = Character.objects.filter(movie_tmdb_id=this_movie[0].tmdb_id)
    # characters = Character.objects.filter(movie_title='The Godfather')
    serializer  = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def comment_this_list(request, movie_pk):
    comments = Movie_Comment.objects.filter(movie=movie_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
    
@api_view(['GET','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Movie_Comment, pk=comment_pk)
    
    if request.method=='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        