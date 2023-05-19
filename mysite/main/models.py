from django.db import models

from accounts.models import CustomUser

class Question_types(models.Model):
    q_type = models.CharField(max_length=50,primary_key=True)




class questionforadmin(models.Model):
    question_text = models.CharField(max_length=200)
    q_type = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=200)
    incorrect_choice1 = models.CharField(max_length=200)
    incorrect_choice2 = models.CharField(max_length=200)
    incorrect_choice3 = models.CharField(max_length=200)
    who_sent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')




# Create your models here.
