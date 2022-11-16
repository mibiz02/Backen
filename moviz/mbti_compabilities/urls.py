from django.urls import path
from . import views

app_name='mbti_compabilities'
urlpatterns = [
    path('',views.character_list),
    path('search/<str:mbti_letter>',views.character_mbti_list),
]