from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q

from .serializer import CharacterSerializer, TypeSerializer, MBTI_CommentSerializer,MBTI_CharacterSerializer
from .models import Character, MBTI_Type, MBTI_Comment
# Create your views here.

@api_view(['GET'])
def character_list(request):
    if request.method == 'GET':
        characters = get_list_or_404(Character)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def character_mbti_list(request, mbti_letter):
    if request.method == 'GET':
        characters = Character.objects.filter(character_MBTI_type=mbti_letter)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def mbti_type_list(request, mbti_letter):
    if request.method == 'GET':
        mbti_types = Character.objects.filter(character_MBTI_type=mbti_letter)
        serializer = TypeSerializer(mbti_types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def character_mbti_good_matching(request, mbti_letter):
    if request.method == 'GET':
        this_mbti_object = MBTI_Type.objects.get(letter=mbti_letter)
        q= Q()
        for el in this_mbti_object.good_matching.all():
            q |= Q(character_MBTI_type=el.letter)

        characters = Character.objects.filter(q)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def character_mbti_bad_matching(request, mbti_letter):
    if request.method == 'GET':
        this_mbti_object = MBTI_Type.objects.get(letter=mbti_letter)
        q= Q()
        bad_matching_lst = []
        for el in this_mbti_object.bad_matching.all():
            bad_matching_lst.append(el.letter)
            q |= Q(character_MBTI_type=el.letter)

        if not bad_matching_lst:
            # 나쁜 관계가 없는 경우: q의 조건을 바꿀것
            characters = Character.objects.filter(id=0)
            serializer = MBTI_CharacterSerializer(characters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            characters = Character.objects.filter(q)
            serializer = MBTI_CharacterSerializer(characters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request,mbti_letter):
    this_mbti_object = get_object_or_404(MBTI_Type, letter=mbti_letter)
    serializer = MBTI_CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(mbti_type=this_mbti_object, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def comment_this_list(request,mbti_letter):
    this_mbti_object = MBTI_Type.objects.get(letter=mbti_letter)
    comment = MBTI_Comment.objects.filter(mbti_type=this_mbti_object.id)
    serializer = MBTI_CommentSerializer(comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(MBTI_Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = MBTI_CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = MBTI_CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
@api_view(['POST'])
def comment_like(request,comment_pk):
    comment = MBTI_Comment.objects.get(pk=comment_pk)
    
    if comment.like_user.filter(pk=request.user.pk).exists():
        comment.like_user.remove(request.user)
        like = False
    else:
        comment.like_user.add(request.user)
        like = True
        
    context = {
        'is_liked' : like
    }
    return Response(context, status=status.HTTP_201_CREATED)
        
    
@api_view(['GET'])
def comment_is_like(request, comment_pk):
    comment = MBTI_Comment.objects.get(pk=comment_pk)
    
    if comment.like_user.filter(pk=request.user.pk).exists():
        is_liked = True
    else:
        is_liked = False
        
    context = {
        'is_liked' : is_liked
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
def mbti_comment_written(request, comment_pk):
    comment = get_object_or_404(MBTI_Comment, pk=comment_pk)
    written = False
    
    if comment.user.pk == request.user.pk:
        written = True
    context = {
        'written' : written
    }
    return Response(context, status=status.HTTP_200_OK)