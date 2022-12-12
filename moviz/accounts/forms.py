
from allauth.account.forms import SignupForm
from django import forms


class SignupForm(SignupForm):
    nickname = forms.CharField(max_length=40, label='Nickname')
    MBTI_type = forms.CharField(max_length=4, label="MBTI Type")

    def custom_signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.MBTI_type = self.cleaned_data['MBTI_type']
        user.save()
        return user
