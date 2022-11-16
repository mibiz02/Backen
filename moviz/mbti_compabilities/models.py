from django.db import models
from django.conf import settings

# Create your models here.
# class MBTI_Type(models.Model):
    # letter = models.CharField(max_length=4)
    # description = models.TextField()
    # good_match = models.ManyToManyField()
    # bad_match = models.ManyToManyField()

# class Comment(models.Model):
#     content = models.TextField()
#     mbti_type = models.ForeignKey(MBTI_Type, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Character(models.Model):
    character_name = models.CharField(max_length=50)
    character_MBTI_type = models.CharField(max_length=4)
    movie_title = models.TextField()
    character_img_path = models.TextField()