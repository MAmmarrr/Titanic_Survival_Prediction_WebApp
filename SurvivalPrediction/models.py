from django.db import models

# Create your models here.

class SurvivalPrediction(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=255)
    image_url = models.CharField(max_length = 2083)
    