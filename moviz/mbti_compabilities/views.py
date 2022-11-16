from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from .serializer import characterSerializer
from .models import Character
# Create your views here.

@api_view(['GET'])
def character_list(request):
    characters = get_list_or_404(Character)
    serializer = characterSerializer(characters, many=True)
    return Response(serializer.data)

