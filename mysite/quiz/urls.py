from django.urls import path
from . import views
app_name = 'quiz'
urlpatterns = [
    path('<str:question_ids>/<str:q_type>/',views.quiz, name='quiz')
]
