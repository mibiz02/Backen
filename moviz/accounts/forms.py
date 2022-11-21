
from allauth.account.forms import SignupForm
from django import forms

# from django.contrib.auth.forms import UserCreationForm

class SignupForm(SignupForm):
    first_name = forms.CharField(max_length=40, label='First Name')
    MBTI_type = forms.CharField(max_length=4, label="MBTI Type")
    last_name = forms.CharField(max_lenth=4, label='Last Name')

    def custom_signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.MBTI_type = self.cleaned_data['MBTI_type']
        user.last_name = self.cleaned_data['last_name']
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
        