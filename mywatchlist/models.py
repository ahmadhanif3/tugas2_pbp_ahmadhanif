from django.db import models

class MyWatchList(models.Model):
    watched = models.CharField(max_length=4)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.TextField()