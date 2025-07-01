from django.shortcuts import render
import requests, random
from .models import Subject, Topic, Question


def home(request):
    return render(request, 'quizapp/home.html')

def create_quiz(request):
    return render(request, 'quizapp/create_quiz.html')
def take_quiz(request):
    subjects = Subject.objects.all()
    topics = []
    questions = []
    selected_subject = None
    selected_topic = None

    if request.method == 'POST':
        selected_subject = request.POST.get('subject')
        selected_topic = request.POST.get('topic')

        if selected_subject:
            topics = Topic.objects.filter(subject_id=selected_subject)

        if selected_topic:
            questions = Question.objects.filter(topic_id=selected_topic).prefetch_related('choices')

    return render(request, 'take_quiz/take_quiz.html', {
        'subjects': subjects,
        'topics': topics,
        'questions': questions,
        'selected_subject': selected_subject,
        'selected_topic': selected_topic
    })

