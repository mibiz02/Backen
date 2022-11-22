from rest_framework import serializers
from .models import Character, MBTI_Type
from .models import MBTI_Comment

class CharacterSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='', read_only=True)

    class Meta:
        model = Character
        fields = '__all__'

class MBTI_CharacterSerializer(serializers.ModelSerializer):
    # character_set = CharacterSerializer(many=True, read_only=True)
    # character_count = serializers.IntegerField(source='character_set.count', read_only=True)

    class Meta:
        model = Character
        fields = '__all__'

class GoodmatchingTypeSerializer(serializers.ModelSerializer):

    class Mets:
        model = MBTI_Type
        fields = ('letter', 'good_matching',)

class BadmatchingTypeSerializer(serializers.ModelSerializer):

    class Mets:
        model = MBTI_Type
        fields = ('letter', 'bad_matching',)

class TypeSerializer(serializers.ModelSerializer):
    # good_matching_for = GoodmatchingTypeSerializer(self, many=True)

    class Meta:
        model = MBTI_Type
        fields = ('letter', 'description')

class MBTI_CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    user_MBTI_type = serializers.CharField(source='user.MBTI_type', read_only=True)
    
    class Meta:
        model = MBTI_Comment
        fields = '__all__'
        read_only_fields = ('mbti_type','user','like_user',)