from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    poster_path = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    release_date = models.TextField()
    genre_name = models.TextField()
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class Movie_Comment(models.Model):
    # movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
     content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
     
    # def __str__(self):
    #     return self.content