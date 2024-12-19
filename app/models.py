from django.db import models

# Create your models here.


class Sports(models.Model):
    sport_name = models.CharField(max_length = 100, primary_key = True)

class Players(models.Model):
    sport_name = models.ForeignKey(Sports, on_delete = models.CASCADE)
    player_name = models.CharField(max_length =  100)
    age =  models.IntegerField()

class Football(models.Model):
    player_name = models.CharField(max_length = 100)
    position = models.CharField(max_length = 100)
    