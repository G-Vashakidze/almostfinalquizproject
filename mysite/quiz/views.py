from django.contrib.auth import logout
from django.shortcuts import render ,redirect
from django.urls import reverse
from .models import Question ,QuizHistory ,Answered
from accounts.models import Achievement

def get_question(question_ids):
    question_ids = question_ids[1:-1]
    question_ids = [int(item) for item in question_ids.split(",")]
    return question_ids

def getting_score(request,q_type,score):
    if QuizHistory.objects.filter(user=request.user, quiz_type=q_type).exists():
        h = QuizHistory.objects.get(user=request.user, quiz_type=q_type)
        if h.high_score < score:
            h.high_score = score
            h.save()
            x = f'congrats you have a new high score {score}'
        else:
            x = f'your score is {score}, your high score is: {h.high_score}'
    else:
        history = QuizHistory(user=request.user, quiz_type=q_type, high_score=score)
        history.save()
        x = QuizHistory(user=request.user, quiz_type=q_type, high_score=score)
        x = x.high_score
        x = f'your score is {score}'
    return x

def check_and_add_achievement(request,name):
    user = request.user
    user_achievements = user.achievements.all()
    has = user_achievements.filter(name=name).exists()
    if not has:
        achievement = Achievement.objects.get(name=name)
        user.achievements.add(achievement)

def check_achivements(request):
    user = request.user
    user.quizes_done +=1
    user.save()
    q_d = user.quizes_done
    if q_d == 1:
        name = 'first quiz'
        achievement = Achievement.objects.get(name=name)
        user.achievements.add(achievement)
    elif q_d == 3:
        name = 'gumbert gumbert'
        achievement = Achievement.objects.get(name=name)
        user.achievements.add(achievement)





def quiz(request, q_type, question_ids):
    template_name = 'quiz/quiz_template.html'
    if request.method == 'POST':
     
        if 'logout' in request.POST:
   
            logout(request)
            err = ''
            return redirect(reverse('accounts:index'),context={'err': err})
        elif 'timersubmit' in request.POST:
            name = 'james may'
            check_and_add_achievement(request,name)
            x = 'Time Out You Failed'
            context = {'done': True, 'x': x, 'q_type': q_type,'question_ids': question_ids}
            return render(request, template_name, context)
        elif 'SBT' in request.POST:
            score = int(request.POST.get('score'))
            x = getting_score(request, q_type=q_type,score=score)
            done = True
            answered_ids = request.POST.get('answered')
            if len(answered_ids)>0:
                ids_list = [int(num) for num in answered_ids.split(",")]
            else:
                ids_list = []
            check_achivements(request)
            if score == 7:
                name = 'monster'
                check_and_add_achievement(request,name)
            for i in ids_list:
                q = Question.objects.get(id=i)
                answered = Answered(user=request.user, question=q)
                answered.save()
            context = {'x':x,'done':done , 'q_type':q_type, 'question_ids':question_ids}
            return render(request, template_name, context)
        elif 'newquiz' or 'qq' in request.POST: 
            print('newquiz')   
            return redirect(reverse('main:QZ'))
    else:
        time = 10
        ids = get_question(question_ids)
        x = 0
        list = []
        for id in ids:
            question = Question.objects.get(q_type=q_type, id=id)
            choices = question.choice_set.all()
            list.append((x,question,choices))
            x+=1
        context = {'list': list, 'q_type': q_type,'question_ids': question_ids ,'time':time}
        return render(request, template_name, context)




  