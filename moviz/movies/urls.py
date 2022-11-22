from django.urls import path
from .  import views

app_name='movies'
urlpatterns = [
    path('', views.movie_lst),
    path('<int:movie_pk>', views.movie_detail),
    path('<int:movie_pk>/character',views.movie_mbti_character),
    path('<int:movie_pk>/comments', views.comment_create),
    path('<int:movie_pk>/this_comments', views.comment_this_list),
    path('comments/<int:comment_pk>', views.comment_detail),
    path('comments/<int:comment_pk>/like', views.comment_like),
]
