from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=128)
    MBTI_type = serializers.CharField(required=False, max_length=4)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['MBTI_type'] = self.validated_data.get('MBTI_type', '')
        return data_dict