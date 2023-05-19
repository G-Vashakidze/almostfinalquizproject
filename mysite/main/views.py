
import random
from django.shortcuts import redirect, render
from accounts.models import CustomUser
from accounts.models import Achievement
from quiz.models import Question , Answered ,Choice ,QuizHistory
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.forms import Myform
from django.contrib.auth import logout
from .models import questionforadmin




def addquestion(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        user = request.user
        if form.is_valid():
            if user.validated:
                data = form.cleaned_data
                question = data['question']
                q_type = data['cat']
                t_q = Question(question_text=question, q_type=q_type)
                t_q.save()
                choices = [[data['correct_answer'],True],[data['incorrect_answer1'],False],[data['incorrect_answer2'],False],[data['incorrect_answer3'],False]]
                random.shuffle(choices)
                for c in choices:
                    choice = Choice(question = t_q, choice_text = c[0], is_correct = c[1])
                    choice.save()
                form = Myform()
                return render(request, 'main/addquestion.html', context={'form':form})
            else:
                data = form.cleaned_data
                question = data['question']
                q_type = data['cat']
                c_c = data['correct_answer']
                ic_c1 = data['incorrect_answer1']
                ic_c2 = data['incorrect_answer2']
                ic_c3 = data['incorrect_answer3']
                q = questionforadmin(question_text = question, q_type=q_type, correct_choice = c_c,incorrect_choice1=ic_c1,incorrect_choice2=ic_c2,incorrect_choice3=ic_c3 ,who_sent = request.user)
                q.save()
                text = 'admin will see youre question and validate'
                return render(request, 'main/addquestion.html', context={'form':form,'text':text})


        
          
    else:
        form = Myform()
    return render(request, 'main/addquestion.html', context={'form':form})



def main(request):
    return render(request, 'main/main.html')


def logout_view(request):
    logout(request)
    
    return redirect(reverse('accounts:index'))




  

def quizes(request):
    if request.method == 'POST':
        q_type = request.POST['button'] 
        user = request.user
        questions_qs = Question.objects.filter(q_type=q_type)
        answered_qs = Answered.objects.filter(user=user, question__q_type=q_type)
        answered_question_ids = answered_qs.values_list('question__id', flat=True)
        remaining_question_ids = list(questions_qs.exclude(id__in=answered_question_ids).values_list('id', flat=True))
        if len(remaining_question_ids) < 1:
            done = True
            return render(request, 'main/main.html', context={'done':done})
        elif len(remaining_question_ids) < 7:
            question_ids = remaining_question_ids
        else:
            question_ids = remaining_question_ids[:7]
        return HttpResponseRedirect(reverse('quiz:quiz', args=(question_ids, q_type)))
    else:
        q_types = list(Question.objects.values_list('q_type',flat=True).distinct())
        return render(request, 'main/quiz_choice.html', context={'q_types':q_types})



def achv(request):
    ac_user = CustomUser.objects.values_list('achievements',flat=True).filter(id=request.user.id)
    achs = Achievement.objects.filter(id__in=ac_user).values_list('name', 'description')
    if len(achs) == 0:
        achs = 'you have no achievements'
    return render(request, 'main/myachivements.html',context={'a':achs})




def leaderboard(request):
    q_types = Question.objects.values_list('q_type', flat=True).distinct()
    x = []
    print(q_types)
    
    for q in q_types:
        y = []
        a = QuizHistory.objects.values_list('user_id','high_score').filter(quiz_type=q).order_by('-high_score')
        l = len(a)
        if l == 0:
            x.append((q,[('no one took quiz', 0)]))
        elif l<5:
            for i in range(l):
                y.append((CustomUser.objects.values_list('username',flat=True).get(id=a[i][0]),a[i][1]))
        else:
            for i in range(5):
                y.append((CustomUser.objects.values_list('username',flat=True).get(id=a[i][0]), a[i][1]))
        x.append((q,y))
    print(x)
    return render(request, 'main/leaderboard.html',context={'x':x})


