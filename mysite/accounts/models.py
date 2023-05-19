from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models



class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    achievements = models.ManyToManyField(Achievement)
    quizes_done = models.IntegerField(default=0)
    validated = models.BooleanField(default=False)

    def add_achievement(self, achievement_name):
        achievement = Achievement.objects.get(name=achievement_name)
        self.achievements.add(achievement)
    



