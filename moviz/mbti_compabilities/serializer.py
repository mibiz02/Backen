from rest_framework import serializers
from .models import Character, MBTI_Type
from .models import MBTI_Comment

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
        fields = ('letter', 'description')

class MBTI_CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MBTI_Comment
        fields = '__all__'
        read_only_fields = ('mbti_type',)