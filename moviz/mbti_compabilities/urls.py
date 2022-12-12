from django.urls import path
from . import views

app_name='mbti_compabilities'
urlpatterns = [
    path('',views.character_list),
    # 특정 MBTI에 해당하는 캐릭터, 특성, 궁합
    path('<str:mbti_letter>',views.character_mbti_list),
    path('type/<str:mbti_letter>',views.mbti_type_list),
    path('type/<str:mbti_letter>/good', views.character_mbti_good_matching),
    path('type/<str:mbti_letter>/bad', views.character_mbti_bad_matching),
    # 댓글 기능
    path('type/<str:mbti_letter>/comment', views.comment_create),
    path('type/<str:mbti_letter>/this_comment', views.comment_this_list),
    path('type/comment/<int:comment_pk>', views.comment_detail),
    path('type/comment/<int:comment_pk>/written', views.mbti_comment_written),
    # 댓글 좋아요 기능
    path('type/comment/<int:comment_pk>/like', views.comment_like),
    path('type/comment/<int:comment_pk>/is_liked', views.comment_is_like),
]