from django.urls import path
from .  import views

app_name='movies'
urlpatterns = [
    path('', views.movie_lst),
    path('/movie/<int:movie_pk>/', views.comment_create),
    path('/movie/<int:movie_pk>/comments/', views.comment_create)
]
