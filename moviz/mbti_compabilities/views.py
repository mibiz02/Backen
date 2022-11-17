from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404
from django.db.models import Q

from .serializer import CharacterSerializer, TypeSerializer
from .models import Character, MBTI_Type
# Create your views here.

@api_view(['GET'])
def character_list(request):
    if request.method == 'GET':
        characters = get_list_or_404(Character)
        serializer = CharacterSerializer(characters, many=True)
        # print(serializer.data)
        return Response(serializer.data)

@api_view(['GET'])
def character_mbti_list(request, mbti_letter):
    if request.method == 'GET':
        characters = Character.objects.filter(character_MBTI_type=mbti_letter)
        print('here')
        serializer = CharacterSerializer(characters, many=True)
        # print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def mbti_type_list(request, mbti_letter):

    mbti_types =MBTI_Type.objects.filter(letter=mbti_letter)
    this_mbti_object = MBTI_Type.objects.get(letter=mbti_letter)
    this_mbti_type_id =MBTI_Type.objects.get(letter=mbti_letter).id
    ideal_matching = MBTI_Type.objects.get(letter=mbti_letter)
    # ideal_matching = MBTI_Type.objects.filter(id=1)
    print('-----------------------------------------------')
    print(this_mbti_object.id)
    print(this_mbti_object.description)
    a = []
    for el in this_mbti_object.good_matching.all():
        a.append(el.id)
    print(a)
    print('-----------------------------------------------')
    serializer = TypeSerializer(mbti_types, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def character_mbti_good_matching(request, mbti_letter):
    this_mbti_object = MBTI_Type.objects.get(letter=mbti_letter)
    good_matching_lst = []
    q= Q()
    for el in this_mbti_object.good_matching.all():
        good_matching_lst.append(el.id)
        q |= Q(id=el.id)

    characters = Character.objects.filter(q)
    # characters = Character.objects.filter(id__in=[6])
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)
