from django.urls import path
from .  import views

app_name='movies'
urlpatterns = [
    path('', views.movie_lst),
    path('<int:movie_pk>', views.movie_detail),
    path('<int:movie_pk>/like', views.movie_like),
    path('<int:movie_pk>/is_liked', views.movie_is_like),
    path('<int:movie_pk>/character',views.movie_mbti_character),
    # 댓글 기능
    path('<int:movie_pk>/comment', views.comment_create),
    path('<int:movie_pk>/this_comments', views.comment_this_list),
    path('comments/<int:comment_pk>', views.comment_detail),
    # 댓글 확인 기능
    path('comments/<int:comment_pk>/written', views.movie_comment_written),
    path('comments/<int:comment_pk>/like', views.comment_like),
    path('comments/<int:comment_pk>/is_liked', views.movie_comment_is_like),
]
