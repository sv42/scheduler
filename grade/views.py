from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Day_grade


def index(request):
    data = {
        'title': 'Оцінки'
    }
    return render(request, 'grade/index.html', data)

def grades(request):
    scores = Day_grade.objects.all() 

    context = {
        'day_grades': scores, 
    }

    return render(request, 'grade/index.html', context)

def user_profile(request):
    user = User.objects.get(id=2) 
    return render(request, 'user_profile.html', {'user': user})