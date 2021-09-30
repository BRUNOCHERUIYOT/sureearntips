from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    date = models.DateField(auto_now_add=True)
    team1 = models.CharField(max_length=200)
    team2 = models.CharField(max_length=200)
    team1odds = models.CharField(max_length=5)
    team2odds = models.CharField(max_length=5)
    placed_bet = models.CharField(max_length=200)
    odds_value = models.CharField(max_length=5)
    game_day = models.DateTimeField()
    history = models.CharField(max_length=400)
    
class users(models.Model):
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    # password = models.CharField(max_length=30)
    # tiptype = models.ForeignKey(Tiptype, on_delete=models.CASCADE)
    
class Tiptype(models.Model):
    daily_tip = models.CharField(max_length=100)
    weekend_tip = models.CharField(max_length=100)
    special_fixed_tip = models.CharField(max_length=100)
    
    def __str__(self):
        return self






class daily_tip(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

class weekend_tip(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)

class special_fixed_tip(models.Model):
    date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)