from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('take-quiz/', views.take_quiz, name='take_quiz'),
    path('create-quiz/', views.create_quiz, name='create_quiz'),
]