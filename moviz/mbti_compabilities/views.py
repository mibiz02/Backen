from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404

from .serializer import CharacterSerializer
from .models import Character
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
        characters = Character.objects.filter(character_MBTI_type__iexact=mbti_letter)
        serializer = CharacterSerializer(characters, many=True)
        # print(serializer.data)
        return Response(serializer.data)
