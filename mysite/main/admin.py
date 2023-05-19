import random
from django.contrib import admin


from quiz.models import Question ,Choice

from .models import questionforadmin

from django.contrib import admin
from .models import questionforadmin

class questionforadminAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'q_type', 'who_sent', 'correct_choice', 'incorrect_choice1', 'incorrect_choice2', 'incorrect_choice3']
    actions = ['validate', 'delete']
    
    def validate(self, request, queryset):
        for question in queryset:
            question_text = question.question_text
            q_type = question.q_type
            correct_choice = question.correct_choice
            incorrect_choice1 = question.incorrect_choice1
            incorrect_choice2 = question.incorrect_choice2
            incorrect_choice3 = question.incorrect_choice3
            validated_question = Question(question_text=question_text, q_type=q_type)
            validated_question.save()
            
    
            validated_choices = [
                (correct_choice, True),
                (incorrect_choice1, False),
                (incorrect_choice2, False),
                (incorrect_choice3, False)
            ]
            for choice_text, is_correct in validated_choices:
                choice = Choice(question=validated_question, choice_text=choice_text, is_correct=is_correct)
                choice.save()
            
    
            who_sent = question.who_sent
            who_sent.validated = True
            who_sent.save()
            
   
            question.delete()
            
    validate.short_description = "Validate selected questions"
    
    def delete(self, request, queryset):
        queryset.delete()
        
admin.site.register(questionforadmin, questionforadminAdmin)






# admin.site.register(questionforadmin)

# class questionforadminAdmin(admin.ModelAdmin):
#     list_display = ['question_text', 'q_type', 'who_sent', 'correct_choice','incorrect_choice1','incorrect_choice2','incorrect_choice3']
#     actions = ['validate','delete']
#     def validate(self ,  queryset):
#         for question in queryset:
#             question_text = question.question_text
#             q_type = question.q_type
#             correct_choice = question.correct_choice
#             incorrect_choice1 = question.incorrect_choice1
#             incorrect_choice2 = question.incorrect_choice2
#             incorrect_choice3 = question.incorrect_choice3
#             who_sent = question.who_sent
#             new_question = Question(question_text=question_text, q_type=q_type)
#             new_question.save()
#             choices = [
#                 (correct_choice, True),
#                 (incorrect_choice1, False),
#                 (incorrect_choice2, False),
#                 (incorrect_choice3, False),
#             ]
#             random.shuffle(choices)
#             for choice_text, is_correct in choices:
#                 choice = Choice(question=new_question, choice_text=choice_text, is_correct=is_correct)
#                 choice.save()
#             who_sent.validated = True
#             who_sent.save()
#             question.delete()
#     validate.short_description = "Validate selected questions"
#     def delete(self, queryset):
#         for question in queryset:
#             question.delete()


# admin.site.register(questionforadmin , questionforadminAdmin)
