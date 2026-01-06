from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)  # Team-Name als Referenz

class Activity(models.Model):
    user_email = models.EmailField()  # User-Email als Referenz
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # Minuten
    date = models.DateField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.JSONField(default=list)  # Liste von User-Emails

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)  # Team-Name als Referenz
    points = models.IntegerField()
