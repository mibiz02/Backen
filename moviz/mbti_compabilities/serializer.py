from rest_framework import serializers
from .models import Character, MBTI_Type

class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = '__all__'

class GoodmatchingTypeSerializer(serializers.ModelSerializer):

    class Mets:
        model = MBTI_Type
        fields = ('letter', 'good_matching',)

class TypeSerializer(serializers.ModelSerializer):
    # good_matching_for = GoodmatchingTypeSerializer(self, many=True)

    class Meta:
        model = MBTI_Type
        fields = ('letter',)

        