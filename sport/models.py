# În fișierul models.py din aplicația ta Django (de exemplu, sportnews/models.py)

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    # Alte câmpuri relevante pentru jucător, cum ar fi poziția, naționalitatea, etc.

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    # Alte câmpuri relevante pentru echipă, cum ar fi țara, antrenorul, etc.

    def __str__(self):
        return self.name