from django.db import models
from django.conf import settings

# Create your models here.
class MBTI_Type(models.Model):
    letter = models.CharField(max_length=4)
    description = models.TextField()
    # good_matching = models.JSONField(null=True)
    good_matching = models.ManyToManyField('self', symmetrical=False, related_name='good_matched')
    # good_matching = models.JSONField(null=True)
    bad_match = models.ManyToManyField('self', symmetrical=True, related_name='bad_matched')
    # type_users = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.id


# class Comment(models.Model):
#     content = models.TextField()
#     mbti_type = models.ForeignKey(MBTI_Type, on_delete=models.CASCADE)
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Character(models.Model):
    character_name = models.CharField(max_length=50)
    character_MBTI_type = models.CharField(max_length=4)
    original_movie_title = models.TextField()
    movie_title = models.TextField()
    character_img_path = models.TextField()