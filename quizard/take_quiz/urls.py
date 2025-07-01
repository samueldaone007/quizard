from django.urls import path
from . import views

app_name = 'take_quiz'

urlpatterns = [
    path('', views.take_quiz, name='take_quiz'),
]