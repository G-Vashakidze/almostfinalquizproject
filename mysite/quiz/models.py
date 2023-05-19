from django.db import models
import requests, random
from accounts.models import CustomUser
import html


class Question (models.Model):
    question_text = models.CharField(max_length=200)
    q_type = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.choice_text

class QuizHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')
    quiz_type = models.CharField(max_length=100)
    high_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.quiz_type} - High Score: {self.high_score}"
    

class Answered(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    

# def add_data_mythology():
#     for i in range(50):
#         resp = requests.get(url="https://opentdb.com/api.php?amount=47&category=20&type=multiple")
#         data = resp.json()['results']
#         for i in data:
#                 if not Question.objects.filter(question_text=i['question']).exists():
#                     x = Question(question_text = i['question'], q_type = 'mythology' )
#                     y = [(i['correct_answer'],True),(i['incorrect_answers'][0],False),(i['incorrect_answers'][1],False),(i['incorrect_answers'][2],False)]
#                     random.shuffle(y)
#                     x.save()
#                     for j in y:
#                         c = Choice(question = x, choice_text = j[0], is_correct = j[1])
#                         c.save()




    # print(x)



# def add_data_animes():
#     for _ in range(50):
#         resp = requests.get(url="https://opentdb.com/api.php?amount=50&category=31&type=multiple")
#         data = resp.json()['results']
#         for item in data:
#             question_text = html.unescape(item['question'])
            
#             if not Question.objects.filter(question_text=question_text).exists():
#                 x = Question(question_text=question_text, q_type='anime')
#                 choices = [
#                     (html.unescape(item['correct_answer']), True),
#                     (html.unescape(item['incorrect_answers'][0]), False),
#                     (html.unescape(item['incorrect_answers'][1]), False),
#                     (html.unescape(item['incorrect_answers'][2]), False)
#                 ]
#                 random.shuffle(choices)
#                 x.save()  
                
#                 for choice_text, is_correct in choices:
#                     c = Choice(question=x, choice_text=choice_text, is_correct=is_correct)
#                     c.save()





# def add_data_animes():
#     for i in range(50):
#         resp = requests.get(url="https://opentdb.com/api.php?amount=50&category=31&type=multiple")
#         data = resp.json()['results']
#         for i in data:
#                 if not Question.objects.filter(question_text=i['question']).exists():
#                     x = Question(question_text = i['question'], q_type = 'anime' )
#                     y = [(i['correct_answer'],True),(i['incorrect_answers'][0],False),(i['incorrect_answers'][1],False),(i['incorrect_answers'][2],False)]
#                     random.shuffle(y)
#                     x.save()
#                     for j in y:
#                         c = Choice(question = x, choice_text = j[0], is_correct = j[1])
#                         c.save()
    