from django.urls import path
from . import views

app_name='mbti_compabilities'
urlpatterns = [
    path('',views.character_list),
    path('<str:mbti_letter>',views.character_mbti_list),
    path('type/<str:mbti_letter>',views.mbti_type_list),
    path('type/<str:mbti_letter>/good', views.character_mbti_good_matching)
    # path('type/<str:mbti_letter>/bad', views.character_mbti_bad_matching)
]