from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    """
    Model for players in the sports team.

    Attributes:
        name (str): The player's name.
        birth_date (DateField): The player's birth date.
        team (ForeignKey): Foreign key to the Team model, representing the player's team.
        history (TextField): Player's history or description.
    """

    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    history = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Returns the string representation of the player (player's name).
        """
        return self.name


class Team(models.Model):
    """
    Model for sports teams.

    Attributes:
        name (str): The team's name.
        coach (str): The team's coach name.
        team_created (DateField): The date the team was created.
    """

    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    team_created = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the team (team's name).
        """
        return self.name


class News(models.Model):
    """
    Model for sports news.

    Attributes:
        title (str): The news title.
        content (TextField): The news content.
        author (ForeignKey): Foreign key to the User model (news author).
        created_at (DateTimeField): The date and time the news was created.
    """

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the news (news title).
        """
        return self.title


class Event(models.Model):
    """
    Model for sports events.

    Attributes:
        name (str): The event name.
        location (str): The event location.
        date (DateField): The event date.
    """

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField(True)

    def __str__(self):
        """
        Returns the string representation of the event (event name).
        """
        return self.name


class Comment(models.Model):
    """
    Model for comments associated with sports events.

    Attributes:
        event (ForeignKey): Foreign key to the Event model (event associated with the comment).
        content (TextField): The comment content.
        user (str): The author's name of the comment.
        created_at (DateTimeField): The date and time the comment was created.
    """

    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the comment (comment details).
        """
        return f'Comment by {self.author} on {self.event.name}'