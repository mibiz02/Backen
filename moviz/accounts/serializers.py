from rest_framework import serializers

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False, max_length=128)
    MBTI_type = serializers.CharField(required=False, max_length=4)
    last_name = serializers.CharField(required=False, max_length=4)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['MBTI_type'] = self.validated_data.get('MBTI_type', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        return data_dict