from django.urls import path
from . import views

app_name='mbti_compabilities'
urlpatterns = [
    path('',views.character_list),
]