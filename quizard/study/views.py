from django.shortcuts import render
import requests

# Create your views here.

def studyer(request):
    return render(request, 'study/study.html')