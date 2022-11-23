from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
    path('',views.user_profile),
    path('like/movie',views.user_like_movie),
]