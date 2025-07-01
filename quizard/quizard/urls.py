from django.contrib import admin
from .import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePage, name='home'),
    path('quizapp/', include('quizapp.urls')),
    path('study/', include('study.urls')),
    path('take_quiz/', include('take_quiz.urls')),
]
