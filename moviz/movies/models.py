from django.db import models

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
    

# class Movie_Comment(models.Model):
    # movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    # user_id = models.ForeignKey(,on_delete=models.CASCADE)
    # content = models.TextField()