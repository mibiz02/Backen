from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    release_date = models.TextField()
    genre_name = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    video_path = models.TextField()
    # movie_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_movies')

    def __str__(self):
        return self.title
    

class Movie_Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # movie_comment_like_users = models.ManyToManyField(settings.AUTH_USER_MOEDL, on_delete=models.CASCADE, related_name='like_movie_comments')
     
    def __str__(self):
        return self.content