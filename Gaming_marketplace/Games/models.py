from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    creator = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField(default=0)