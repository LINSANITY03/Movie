from django.db import models

import datetime
# Create your models here.

class MOVIE_STATUS(models.IntegerChoices):
    COMING_UP = 1, 'COMING_UP'
    STARTING = 2, 'STARTING'
    RUNNING = 3, 'RUNNING'
    FINISHED = 4, 'FINISHED'

class Movie(models.Model):
    class Meta:
        db_table = 'Movie'

    name = models.CharField(max_length=200, null=False, blank=False)
    protagonists = models.TextField(null=False, blank=False)
    poster = models.ImageField(upload_to='images/Movie_poster', blank=False, null=False)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    status = models.IntegerField(choices=MOVIE_STATUS.choices, default=MOVIE_STATUS.COMING_UP)
    ranking = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name} starring {self.protagonists} at {self.start_date}"