from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('quizes/', views.quizes, name='QZ'),
    path('',views.main, name='main'),
    path('addquestion/', views.addquestion, name='AQ'),
    path('leaderboard/', views.leaderboard, name='LD'),
    path('myachivements/', views.achv, name='MA'),
    path('lg/', views.logout_view, name='LG'),
    


]