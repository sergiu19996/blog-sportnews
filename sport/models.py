from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.event.name}'