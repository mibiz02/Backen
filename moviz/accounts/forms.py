
from allauth.account.forms import SignupForm
from django import forms

# from django.contrib.auth.forms import UserCreationForm

class SignupForm(SignupForm):
    nickname = forms.CharField(max_length=40, label='Nickname')
    MBTI_type = forms.CharField(max_length=4, label="MBTI Type")

    def custom_signup(self, request, user):
        user.nickname = self.cleaned_data['nickname']
        user.MBTI_type = self.cleaned_data['MBTI_type']
        user.save()
        return user

# #첫번째 시도-url을 변경하면 csrf 문제가 발생
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('email','first_name',)
# from allauth.account.forms import SignupForm,LoginForm
# from django import forms

# class MyCustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#         self.fields['MBTI_Tye'] = forms.CharField(required=True)


# class MyCustomLoginForm(LoginForm):
#     def __int__(self, *args, **kwargs):
#         super(MyCustomLoginForm, self).__init__(*args, **kwargs)
#         self.fields['login'].widget = forms.Tex
        