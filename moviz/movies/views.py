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
# @permission_classes([IsAuthenticated])
def movie_lst(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_mbti_character(request, movie_pk):
    if request.method == 'GET':
        this_movie = Movie.objects.filter(pk=movie_pk)
        characters = Character.objects.filter(movie_tmdb_id=this_movie[0].tmdb_id)
        serializer  = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_this_list(request, movie_pk):
    comments = Movie_Comment.objects.filter(movie=movie_pk)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@api_view(['GET','DELETE','PUT'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Movie_Comment, pk=comment_pk)
    
    if request.method=='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
@api_view(['POST'])
def comment_like(request, comment_pk):
    comment = Movie_Comment.objects.get(pk=comment_pk)
    
    if comment.movie_comment_like_users.filter(pk=request.user.pk).exists():
        comment.movie_comment_like_users.remove(request.user)
        is_liked = False
    else:
        comment.movie_comment_like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked' : is_liked
    }
    return Response(context, status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        movie.movie_like_users.remove(request.user)
        is_liked = False
    else:
        movie.movie_like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked' : is_liked
    }
    return Response(context, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_is_like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    
    if movie.movie_like_users.filter(pk=request.user.pk).exists():
        is_liked = True
    else:
        is_liked = False
    context = {
        'is_liked' : is_liked
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_comment_is_like(request, comment_pk):
    movie_comment = Movie_Comment.objects.get(pk=comment_pk)
    
    if movie_comment.movie_comment_like_users.filter(pk=request.user.pk).exists():
        is_liked = True
    else:
        is_liked = False
    context = {
        'is_liked' : is_liked
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_comment_written(request, comment_pk):
    movie_comment = Movie_Comment.objects.get(pk=comment_pk)
    written = False
    if movie_comment.user.pk == request.user.pk:
        written = True
    context = {
        'written' : written
    }
    return Response(context, status=status.HTTP_200_OK)